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

<div class="modal fade" id="moduleActionModal" tabindex="-1" role="dialog" aria-labelledby="moduleActionModalCenterTitle" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h4 class="uninstall action_available modal-title" id="moduleActionlModalLongTitle">{l s='Uninstall module?' mod='ps_themecusto'}</h4>
                <h4 class="disable action_available modal-title" id="moduleActionlModalLongTitle">{l s='Disable module?' mod='ps_themecusto'}</h4>
                <h4 class="reset action_available modal-title" id="moduleActionlModalLongTitle">{l s='Reset module?' mod='ps_themecusto'}</h4>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                <div class="uninstall action_available">
                    <p>{l s='You are about to uninstall' mod='ps_themecusto'} <span class="module-displayname" ></span></p>
                    <p>{l s='This will definitely disable the module.' mod='ps_themecusto'}</p>
                </div>
                <div class="disable action_available">
                    <p>{l s='You are about to disable ' mod='ps_themecusto'} <span class="module-displayname" ></span></p>
                    <p>{l s='Your current settings will be saved, but the module will no longer be active.' mod='ps_themecusto'}</p>
                </div>
                <div class="reset action_available">
                    <p>{l s='You are about to reset ' mod='ps_themecusto'} <span class="module-displayname" ></span></p>
                    <p>{l s='This will restore the defaults settings.' mod='ps_themecusto'}</p>
                    <p>{l s='This action cannot be undone.' mod='ps_themecusto'}</p>
                </div>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">{l s='Cancel' mod='ps_themecusto'}</button>
                <a class="btn btn-primary uppercase" href="#" data-dismiss="modal" data-action="false" data-name="false" data-deletion="true">
                    <span class="uninstall action_available">{l s='Yes, uninstall it' mod='ps_themecusto'}</span>
                    <span class="disable action_available">{l s='Yes, disable it' mod='ps_themecusto'}</span>
                    <span class="reset action_available">{l s='Yes, reset it' mod='ps_themecusto'}</span>
                </a>
            </div>
        </div>
    </div>
</div>