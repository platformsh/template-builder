{*
* 2007-2018 PrestaShop
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
*  @author    PrestaShop SA <contact@prestashop.com>
*  @copyright 2007-2018 PrestaShop SA
*  @license   http://opensource.org/licenses/afl-3.0.php  Academic Free License (AFL 3.0)
*  International Registered Trademark & Property of PrestaShop SA
*}

<div id="modulecontent" class="clearfix">
    <div id="faviconbo-menu">
        <div class="col-lg-2">
            <div class="list-group" v-on:click.prevent>
                <a href="#" class="list-group-item" v-bind:class="{ 'active': isActive('faviconConfiguration') }" v-on:click="makeActive('faviconConfiguration')"><i class="fa fa-gavel"></i> {l s='Get started' d='Modules.Faviconnotificationbo.Admin'}</a>
            </div>
            <div class="list-group" v-on:click.prevent>
                <a class="list-group-item" style="text-align:center"><i class="icon-info"></i> {l s='Version' d='Admin.Global'} {$module_version|escape:'htmlall':'UTF-8'} | <i class="icon-info"></i> PrestaShop {$ps_version|escape:'htmlall':'UTF-8'}</a>
            </div>
        </div>
    </div>

    {* list your admin tpl *}
    <div id="faviconConfiguration" class="faviconbo_menu addons-hide">
        {include file="./tabs/faviconConfiguration.tpl"}
    </div>

</div>

{* Use this if you want to send php var to your js *}
{literal}
<script type="text/javascript">
    var base_url = "{/literal}{$ps_base_dir|escape:'htmlall':'UTF-8'}{literal}";
    var isPs17 = "{/literal}{$isPs17|escape:'htmlall':'UTF-8'}{literal}";
    var currentPage = "{/literal}{$currentPage|escape:'htmlall':'UTF-8'}{literal}";
    var moduleAdminLink = "{/literal}{$moduleAdminLink|escape:'htmlall':'UTF-8'}{literal}";
    var moduleName = "{/literal}{$module_name|escape:'htmlall':'UTF-8'}{literal}";
    var ps_version = "{/literal}{$isPs17|escape:'htmlall':'UTF-8'}{literal}";
</script>
{/literal}
