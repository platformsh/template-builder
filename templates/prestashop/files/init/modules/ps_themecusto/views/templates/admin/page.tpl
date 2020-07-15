{*
* 2007-2018 PrestaShop
*
* DISCLAIMER
*
* Do not edit or add to this file if you wish to upgrade PrestaShop to newer
* versions in the future. If you wish to customize PrestaShop for your
* needs please refer to http://www.prestashop.com for more information.
*
* @author    PrestaShop SA <contact@prestashop.com>
* @copyright 2007-2018 PrestaShop SA
* @license   http://addons.prestashop.com/en/content/12-terms-and-conditions-of-use
* International Registered Trademark & Property of PrestaShop SA
*}

<div class="content-div">
    <div class="grid">
        <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
            {if $enable}
                {include file="./controllers/$configure_type/index.tpl"}
            {else}
                <div class="panel col-lg-12 col-md-12 col-sm-12 col-xs-12">
                    <h4>{l s='The module %s has been disabled' sprintf=$moduleName mod='ps_themecusto'}</h4>
                </div>
            {/if}
        </div>
    </div>
</div>
