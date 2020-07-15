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

<div class="modal fade" id="upload-child-modal" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
                <h4 class="modal-title module-modal-title" id="exampleModalLongTitle">{l s='Upload child theme' mod='ps_themecusto'}</h4>
            </div>
            <div class="modal-body">
                <div class="row">
                    <div class="col-md-12">
                        <form action="#" class="dropzone dz-clickable" id="importDropzone">
                            <div class="loader"></div>
                            <div class="module-import-start">
                                <i class="module-import-start-icon material-icons">cloud_upload</i><br>
                                <p class="module-import-start-main-text">
                                    {l s='Drop your child theme archive here or' mod='ps_themecusto'} <a href="#" class="module-import-start-select-manual">{l s='select file' mod='ps_themecusto'}</a>
                                </p>
                                <p class="module-import-start-footer-text">
                                    {l s='Please upload one file at a time, .zip. Your child theme will be installed right after that.' mod='ps_themecusto'}
                                </p>
                            </div>
                            <div class="module-import-failure">
                                <i class="module-import-failure-icon material-icons">error</i><br>
                                <p class="module-import-failure-msg">{l s='Oops... Upload failed.' mod='ps_themecusto'}</p>
                                <a href="#" class="module-import-failure-details-action">{l s='What happened?' mod='ps_themecusto'}</a>
                                <div class="module-import-failure-details">{l s='An error has occurred.' mod='ps_themecusto'}</div>
                                <p>
                                    <a class="module-import-failure-retry btn btn-tertiary" href="#">{l s='Try again' mod='ps_themecusto'}</a>
                                </p>
                            </div>
                            <div class="module-import-success">
                                <i class="module-import-success-icon material-icons">done</i><br>
                                <p class="module-import-success-msg"></p>
                            </div>
                            <input type="hidden" name="action" value="UploadChildTheme" />
                            <div class="dz-default dz-message"><span></span></div><input name="childthemefile" type="file" class="dz-hidden-input" accept=".zip" style="visibility: hidden; position: absolute; top: 0px; left: 0px; height: 0px; width: 0px;">
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>