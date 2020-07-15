<?php

class LinkBlockPresenter
{
    private $link;
    private $language;

    public function __construct(Link $link, Language $language)
    {
        $this->link = $link;
        $this->language = $language;
    }

    public function present(LinkBlock $cmsBlock)
    {
        return array(
            'id' => (int)$cmsBlock->id,
            'title' => $cmsBlock->name[(int)$this->language->id],
            'hook' => (new Hook((int)$cmsBlock->id_hook))->name,
            'position' => $cmsBlock->position,
            'links' => $this->makeLinks($cmsBlock->content, $cmsBlock->custom_content),
        );
    }

    private function makeLinks($content, $custom_content)
    {
        $cmsLinks = $productLinks = $staticsLinks = $customLinks = array();

        if (isset($content['cms'])) {
            $cmsLinks = $this->makeCmsLinks($content['cms']);
        }

        if (isset($content['product'])) {
            $productLinks = $this->makeProductLinks($content['product']);
        }

        if (isset($content['static'])) {
            $staticsLinks = $this->makeStaticLinks($content['static']);
        }

        $customLinks = $this->makeCustomLinks($custom_content);

        return array_merge(
            $cmsLinks,
            $productLinks,
            $staticsLinks,
            $customLinks
        );
    }

    private function makeCmsLinks($cmsIds)
    {
        $cmsLinks = array();
        foreach ($cmsIds as $cmsId) {
            $cms = new CMS((int)$cmsId);
            if (null !== $cms->id && $cms->active) {
                $cmsLinks[] = array(
                    'id' => 'link-cms-page-'.$cms->id,
                    'class' => 'cms-page-link',
                    'title' => $cms->meta_title[(int)$this->language->id],
                    'description' => $cms->meta_description[(int)$this->language->id],
                    'url' => $this->link->getCMSLink($cms),
                );
            }
        }

        return $cmsLinks;
    }

    private function makeProductLinks($productIds)
    {
        $productLinks = array();
        foreach ($productIds as $productId) {
            if (false !== $productId) {
                $meta = Meta::getMetaByPage($productId, (int)$this->language->id);
                $productLinks[] = array(
                    'id' => 'link-product-page-'.$productId,
                    'class' => 'cms-page-link',
                    'title' => $meta['title'],
                    'description' => $meta['description'],
                    'url' => $this->link->getPageLink($productId, true),
                );
            }
        }

        return $productLinks;
    }

    private function makeStaticLinks($staticIds)
    {
        $staticLinks = array();
        foreach ($staticIds as $staticId) {
            if (false !== $staticId) {
                $meta = Meta::getMetaByPage($staticId, (int)$this->language->id);
                $staticLinks[] = array(
                    'id' => 'link-static-page-'.$staticId,
                    'class' => 'cms-page-link',
                    'title' => $meta['title'],
                    'description' => $meta['description'],
                    'url' => $this->link->getPageLink($staticId, true),
                );
            }
        }

        return $staticLinks;
    }

    private function makeCustomLinks($customContent)
    {
        $customLinks = array();

        if (isset($customContent[$this->language->id])) {
            $customLinks = $customContent[$this->language->id];

            $customLinks = array_map(function ($el) {
                return array(
                    'id' => 'link-custom-page-'.$el['title'],
                    'class' => 'custom-page-link',
                    'title' => $el['title'],
                    'description' => '',
                    'url' => $el['url'],
                    'target' => $this->isExternalLink($el['url']) ? '_blank' : '',
                );
            },
            array_filter($customLinks));
        }

        return $customLinks;
    }

    /**
     * Check the url if is an external link
     * @param $url
     * @return bool
     */
    private function isExternalLink($url)
    {
        $baseLink = preg_replace('#^(http)s?://#', '', $this->link->getBaseLink());
        $url = strtolower($url);

        if (preg_match('#^(http)s?://#', $url) && !preg_match('#^(http)s?://' . preg_quote(rtrim($baseLink, '/'), '/') . '#', $url)) {
            return true;
        }

        return false;
    }

}
