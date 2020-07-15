<?php
/**
 * 2007-2016 PrestaShop
 *
 * NOTICE OF LICENSE
 *
 * This source file is subject to the Academic Free License (AFL 3.0)
 * that is bundled with this package in the file LICENSE.txt.
 * It is also available through the world-wide-web at this URL:
 * http://opensource.org/licenses/afl-3.0.php
 * If you did not receive a copy of the license and are unable to
 * obtain it through the world-wide-web, please send an email
 * to license@prestashop.com so we can send you a copy immediately.
 *
 * DISCLAIMER
 *
 * Do not edit or add to this file if you wish to upgrade PrestaShop to newer
 * versions in the future. If you wish to customize PrestaShop for your
 * needs please refer to http://www.prestashop.com for more information.
 *
 * @author    PrestaShop SA <contact@prestashop.com>
 * @copyright 2007-2015 PrestaShop SA
 * @license   http://opensource.org/licenses/afl-3.0.php  Academic Free License (AFL 3.0)
 * International Registered Trademark & Property of PrestaShop SA
 */

namespace OnBoarding;

use Module;
use PrestaShopBundle\Service\Routing\Router;

class Configuration
{
    /**
     * Module Dependency
     */
    const MODULE_MBO = 'ps_mbo';

    const FAKE_ID = 123456789;

    private $translator;

    public function __construct($translator)
    {
        $this->translator = $translator;
    }

    public function getConfiguration(Router $router)
    {
        $contextLink = \Context::getContext()->link;

        $productFormUrlPattern = $this->generateSfBaseUrl(
            $router,
            'admin_product_form',
            ['id' => static::FAKE_ID]
        );


        $data = [
            'templates' => [
                'lost',
                'popup',
                'tooltip',
            ],
            'steps' => [
                'groups' => [
                    [
                        'steps' => [
                            [
                                'type' => 'popup',
                                'text' => [
                                    'type' => 'template',
                                    'src' => 'welcome',
                                ],
                                'options' => [
                                    'savepoint',
                                    'hideFooter',
                                ],
                                'page' => $contextLink->getAdminLink('AdminDashboard'),
                            ],
                        ],
                    ],
                    [
                        'title' => $this->translator->trans('Let\'s create your first product', [], 'Modules.Welcome.Admin'),
                        'subtitle' => [
                            '1' => $this->translator->trans('What do you want to tell about it? Think about what your customers want to know.', [], 'Modules.Welcome.Admin'),
                            '2' => $this->translator->trans('Add clear and attractive information. Don\'t worry, you can edit it later :)', [], 'Modules.Welcome.Admin'),
                        ],
                        'steps' => [
                            [
                                'type' => 'tooltip',
                                'text' => $this->translator->trans('Give your product a catchy name.', [], 'Modules.Welcome.Admin'),
                                'options' => [
                                    'savepoint',
                                ],
                                'page' => [
                                    $router->generate('admin_product_new'),
                                    $productFormUrlPattern,
                                ],
                                'selector' => '#form_step1_name_1',
                                'position' => 'right',
                            ],
                            [
                                'type' => 'tooltip',
                                'text' => $this->translator->trans('Fill out the essential details in this tab. The other tabs are for more advanced information.', [], 'Modules.Welcome.Admin'),
                                'page' => $productFormUrlPattern,
                                'selector' => '#tab_step1',
                                'position' => 'right',
                            ],
                            [
                                'type' => 'tooltip',
                                'text' => $this->translator->trans('Add one or more pictures so your product looks tempting!', [], 'Modules.Welcome.Admin'),
                                'page' => $productFormUrlPattern,
                                'selector' => '#product-images-dropzone',
                                'position' => 'right',
                            ],
                            [
                                'type' => 'tooltip',
                                'text' => $this->translator->trans('How much do you want to sell it for?', [], 'Modules.Welcome.Admin'),
                                'page' => $productFormUrlPattern,
                                'selector' => '.right-column > .row > .col-md-12 > .form-group:nth-child(4) > .row > .col-md-6:first-child > .input-group',
                                'position' => 'left',
                                'action' => [
                                    'selector' => '#product_form_save_go_to_catalog_btn',
                                    'action' => 'click',
                                ],
                            ],
                            [
                                'type' => 'tooltip',
                                'text' => $this->translator->trans('Yay! You just created your first product. Looks good, right?', [], 'Modules.Welcome.Admin'),
                                'page' => $this->generateSfBaseUrl($router, 'admin_product_catalog'),
                                'selector' => '#product_catalog_list table tr:first-child td:nth-child(3)',
                                'position' => 'left',
                            ],
                        ],
                    ],
                    [
                        'title' => $this->translator->trans('Give your shop its own identity', [], 'Modules.Welcome.Admin'),
                        'subtitle' => [
                            '1' => $this->translator->trans('How do you want your shop to look? What makes it so special?', [], 'Modules.Welcome.Admin'),
                            '2' => $this->translator->trans('Customize your theme or choose the best design from our theme catalog.', [], 'Modules.Welcome.Admin'),
                        ],
                        'steps' => [
                            [
                                'type' => 'tooltip',
                                'text' => $this->translator->trans('A good way to start is to add your own logo here!', [], 'Modules.Welcome.Admin'),
                                'options' => [
                                    'savepoint',
                                ],
                                'page' => $contextLink->getAdminLink('AdminThemes'),
                                'selector' => '#js_theme_form_container .tab-content.panel .btn:first-child',
                                'position' => 'right',
                            ],
                            [
                                'type' => 'tooltip',
                                'text' => $this->translator->trans('If you want something really special, have a look at the theme catalog!', [], 'Modules.Welcome.Admin'),
                                'page' => $contextLink->getAdminLink('AdminThemesCatalog'),
                                'selector' => '.addons-theme-one:first-child',
                                'position' => 'right',
                            ],
                        ],
                    ],
                ],
            ],
        ];

        $paymentSteps = [
            'title' => $this->translator->trans('Get your shop ready for payments', [], 'Modules.Welcome.Admin'),
            'subtitle' => [
                '1' => $this->translator->trans('How do you want your customers to pay you?', [], 'Modules.Welcome.Admin'),
            ],
            'steps' => [
                [
                    'type' => 'tooltip',
                    'text' => $this->translator->trans('These payment methods are already available to your customers.', [], 'Modules.Welcome.Admin'),
                    'options' => [
                        'savepoint',
                    ],
                    'page' => $contextLink->getAdminLink('AdminPayment'),
                    'selector' => '.modules_list_container_tab:first tr:first-child .text-muted, .card:eq(0) .text-muted:eq(0)',
                    'position' => 'right',
                ],
            ],
        ];

        if (Module::isInstalled(self::MODULE_MBO) && Module::isEnabled(self::MODULE_MBO)) {
            $paymentSteps['subtitle']['2'] = $this->translator->trans(
                'Adapt your offer to your market: add the most popular payment methods for your customers!',
                [],
                'Modules.Welcome.Admin'
            );
            $paymentSteps['steps'][] = [
                'type' => 'tooltip',
                'text' => $this->translator->trans('And you can choose to add other payment methods from here!', [], 'Modules.Welcome.Admin'),
                'page' => $contextLink->getAdminLink('AdminPayment'),
                'selector' => '.panel:eq(1) table tr:eq(0) td:eq(1), .card:eq(1) .module-item-list div:eq(0) div:eq(1)',
                'position' => 'top',
            ];
        }
        $data['steps']['groups'][] = $paymentSteps;

        $shippingSteps = [
            'title' => $this->translator->trans('Choose your shipping solutions', [], 'Modules.Welcome.Admin'),
            'subtitle' => [
                '1' => $this->translator->trans('How do you want to deliver your products?', [], 'Modules.Welcome.Admin'),
            ],
            'steps' => [
                [
                    'type' => 'tooltip',
                    'text' => $this->translator->trans('Here are the shipping methods available on your shop today.', [], 'Modules.Welcome.Admin'),
                    'options' => [
                        'savepoint',
                    ],
                    'page' => $contextLink->getAdminLink('AdminCarriers'),
                    'selector' => '#table-carrier tr:eq(2) td:eq(3)',
                    'position' => 'right',
                ],
            ],
        ];

        if (Module::isInstalled(self::MODULE_MBO) && Module::isEnabled(self::MODULE_MBO)) {
            $shippingSteps['subtitle']['2'] = $this->translator->trans(
                'Select the shipping solutions the most likely to suit your customers! Create your own carrier or add a ready-made module.',
                [],
                'Modules.Welcome.Admin'
            );

            $shippingSteps['steps'][] = [
                'type' => 'tooltip',
                'text' => $this->translator->trans('You can offer more delivery options by setting up additional carriers', [], 'Modules.Welcome.Admin'),
                'page' => $contextLink->getAdminLink('AdminCarriers'),
                'selector' => '.modules_list_container_tab tr:eq(0) .text-muted',
                'position' => 'right',
            ];
        }
        $data['steps']['groups'][] = $shippingSteps;


        $moduleSteps = [
            'title' => $this->translator->trans('Improve your shop with modules', [], 'Modules.Welcome.Admin'),
            'subtitle' => [
                '1' => $this->translator->trans('Add new features and manage existing ones thanks to modules.', [], 'Modules.Welcome.Admin'),
                '2' => $this->translator->trans('Some modules are already pre-installed, others may be free or paid modules - browse our selection and find out what is available!', [], 'Modules.Welcome.Admin'),
            ],
            'steps' => [
                [
                    'type' => 'tooltip',
                    'text' => $this->translator->trans('Discover our module selection in the first tab. Manage your modules on the second one and be aware of notifications in the third tab.', [], 'Modules.Welcome.Admin'),
                    'options' => [
                        'savepoint',
                    ],
                    'page' => $router->generate('admin_module_catalog'),
                    'selector' => '.page-head-tabs .tab:eq(0)',
                    'position' => 'right',
                ],
                [
                    'type' => 'popup',
                    'text' => [
                        'type' => 'template',
                        'src' => 'end',
                    ],
                    'options' => [
                        'savepoint',
                        'hideFooter',
                    ],
                    'page' => $this->generateSfBaseUrl($router, 'admin_module_catalog'),
                ],
            ],
        ];
        $data['steps']['groups'][] = $moduleSteps;

        return $data;
    }

    /**
     * generate url pattern to recognize the route as the current step url
     * here we replace the route specific parameters with wildcard to allow regexp matching
     *
     * @param \PrestaShopBundle\Service\Routing\Router $router
     * @param                                          $controller
     * @param array                                    $fakeParameters
     *
     * @return mixed|string
     */
    protected function generateSfBaseUrl(Router $router, $controller, $fakeParameters = [])
    {
        $url = $router->getGenerator()->generate($controller, $fakeParameters);
        $url = substr($url, strlen(basename(__PS_BASE_URI__)) + 1);
        $url = str_replace('/' . basename(_PS_ADMIN_DIR_) . '/', '', $url);

        $url = str_replace(array_values($fakeParameters), '.+', $url);

        return $url;
    }
}
