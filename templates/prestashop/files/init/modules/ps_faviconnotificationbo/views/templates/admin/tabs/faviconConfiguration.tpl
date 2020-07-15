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
<div class="panel col-lg-10 right-panel">
    <form method="post" action="{$moduleAdminLink|escape:'htmlall':'UTF-8'}&page=faviconConfiguration" class="form-horizontal">
        <h3>
            {l s='Configuration' d='Admin.Global'}
        </h3>
        <div class="form-group row">
            <div class="title">
                {l s='Display notifications in the browser tab for:' d='Modules.Faviconnotificationbo.Admin'}
            </div>
            <ol>
                <div class="col-lg-5 col-md-4 col-xs-10">
                    <div class="form-group">
                        <div class="control-label col-lg-5 col-md-4 col-xs-10">
                            <label class="labelbutton">{l s='New orders' d='Modules.Faviconnotificationbo.Admin'}</label>
                        </div>
                        <div>
                            <div class="input-group fixed-width-lg">
                                <span class="switch prestashop-switch fixed-width-lg">
                                <input class="yes" type="radio" name="CHECKBOX_ORDER" id="checkbox_track_new_orders_on" value="1" {if $bofavicon_params.CHECKBOX_ORDER eq 1}checked="checked"{/if}>
                                <label for="checkbox_track_new_orders_on" class="radioCheck">{l s='Yes' d='Admin.Global'}</label>
                                <input class="no" type="radio" name="CHECKBOX_ORDER" id="checkbox_track_new_orders_off" value="0" {if $bofavicon_params.CHECKBOX_ORDER eq 0}checked="checked"{/if}>
                                <label for="checkbox_track_new_orders_off" class="radioCheck">{l s='No' d='Admin.Global'}</label>
                                <a class="slide-button btn"></a>
                                </span>
                            </div>
                        </div>
                    </div>
                    <div class="form-group">
                        <div class="control-label col-lg-5 col-md-4 col-xs-10">
                            <label class="labelbutton">{l s='New customers' d='Admin.Navigation.Header'}</label>
                        </div>
                        <div>
                            <div class="input-group fixed-width-lg">
                                <span class="switch prestashop-switch fixed-width-lg">
                                <input class="yes" type="radio" name="CHECKBOX_CUSTOMER" id="checkbox_track_new_customers_on" value="1" {if $bofavicon_params.CHECKBOX_CUSTOMER eq 1}checked="checked"{/if}>
                                <label for="checkbox_track_new_customers_on" class="radioCheck">{l s='Yes' d='Admin.Global'}</label>
                                <input class="no" type="radio" name="CHECKBOX_CUSTOMER" id="checkbox_track_new_customers_off" value="0" {if $bofavicon_params.CHECKBOX_CUSTOMER eq 0}checked="checked"{/if}>
                                <label for="checkbox_track_new_customers_off" class="radioCheck">{l s='No' d='Admin.Global'}</label>
                                <a class="slide-button btn"></a>
                                </span>
                            </div>
                        </div>
                    </div>
                    <div class="form-group">
                        <div class="control-label col-lg-5 col-md-4 col-xs-10">
                            <label class="labelbutton">{l s='New messages' d='Admin.Orderscustomers.Feature'}</label>
                        </div>
                        <div>
                            <div class="input-group fixed-width-lg">
                                <span class="switch prestashop-switch fixed-width-lg">
                                <input class="yes" type="radio" name="CHECKBOX_MESSAGE" id="checkbox_track_new_messages_on" value="1" {if $bofavicon_params.CHECKBOX_MESSAGE eq 1}checked="checked"{/if}>
                                <label for="checkbox_track_new_messages_on" class="radioCheck">{l s='Yes' d='Admin.Global'}</label>
                                <input class="no" type="radio" name="CHECKBOX_MESSAGE" id="checkbox_track_new_messages_off" value="0" {if $bofavicon_params.CHECKBOX_MESSAGE eq 0}checked="checked"{/if}>
                                <label for="checkbox_track_new_messages_off" class="radioCheck">{l s='No' d='Admin.Global'}</label>
                                <a class="slide-button btn"></a>
                                </span>
                            </div>
                        </div>
                    </div>
                </div>
            </ol>
        </div>
        <div class="col-lg-5">
            <div class="form-group">
                <div class="divcolorpicker control-label col-lg-6 col-md-4 col-xs-10">
                    <label class="labelbutton" for="faviconbo_input_backgroundcolor">{l s='Notification background color' d='Modules.Faviconnotificationbo.Admin'}</label>
                </div>
                <div>
                    <div class="input-group fixed-width-lg">
                        <input id="BACKGROUND_COLOR_FAVICONBO" type="text" data-hex="true" class="mColorPickerFaviconInput" value="{if isset($bofavicon_params.BACKGROUND_COLOR_FAVICONBO)}{$bofavicon_params.BACKGROUND_COLOR_FAVICONBO|escape:'quotes'}{/if}" name="BACKGROUND_COLOR_FAVICONBO"/>
                    </div>
                </div>
            </div>
            <div class="form-group">
                <div class="divcolorpicker control-label col-lg-6 col-md-4 col-xs-10">
                    <label class="labelbutton" for="faviconbo_input_textcolor">{l s='Notification text color' d='Modules.Faviconnotificationbo.Admin'}</label>
                </div>
                <div>
                    <div class="input-group fixed-width-lg">
                        <input id="TEXT_COLOR_FAVICONBO" type="text" data-hex="true" class="mColorPickerFaviconInput" value="{if isset($bofavicon_params.TEXT_COLOR_FAVICONBO)}{$bofavicon_params.TEXT_COLOR_FAVICONBO|escape:'quotes'}{/if}" name="TEXT_COLOR_FAVICONBO"/>
                    </div>
                </div>
            </div>
        </div>
        <div class="panel-footer">
            <button type="submit" value="1" id="module_form_submit_btn" name="submitFavIconConf" class="btn btn-default pull-right"><i class="process-icon-save"></i>{l s='Save' d='Admin.Actions'}</button>
        </div>
    </form>
</div>
