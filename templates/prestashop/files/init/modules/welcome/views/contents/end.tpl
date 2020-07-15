{*
2007-2016 PrestaShop

NOTICE OF LICENSE

This source file is subject to the Academic Free License (AFL 3.0)
that is bundled with this package in the file LICENSE.txt.
It is also available through the world-wide-web at this URL:
http://opensource.org/licenses/afl-3.0.php
If you did not receive a copy of the license and are unable to
obtain it through the world-wide-web, please send an email
to license@prestashop.com so we can send you a copy immediately.

DISCLAIMER

Do not edit or add to this file if you wish to upgrade PrestaShop to newer
versions in the future. If you wish to customize PrestaShop for your
needs please refer to http://www.prestashop.com for more information.

@author    PrestaShop SA <contact@prestashop.com>
@copyright 2007-2016 PrestaShop SA
@license   http://opensource.org/licenses/afl-3.0.php  Academic Free License (AFL 3.0)
International Registered Trademark & Property of PrestaShop SA
*}

<div id="onboarding-welcome" class="modal-body">
    <div class="col-12">
        <button class="onboarding-button-next pull-right close" type="button">&times;</button>
        <h2 class="text-center text-md-center">{l s='Over to you!' d='Modules.Welcome.Admin'}</h2>
    </div>
    <div class="col-12">
        <p class="text-center text-md-center">
          {l s='You\'ve seen the essential, but there\'s a lot more to explore.' d='Modules.Welcome.Admin'}<br />
          {l s='Some ressources can help you go further:' d='Modules.Welcome.Admin'}
        </p>
        <div class="container-fluid">
          <div class="row">
            <div class="col-md-6  justify-content-center text-center text-md-center link-container">
              <a class="final-link" href="http://doc.prestashop.com/display/PS17/Getting+Started" target="_blank">
                <div class="starter-guide"></div>
                <span class="link">{l s='Starter Guide' d='Modules.Welcome.Admin'}</span>
              </a>
            </div>
            <div class="col-md-6 text-center text-md-center link-container">
              <a class="final-link" href="https://www.prestashop.com/forums/" target="_blank">
                <div class="forum"></div>
                <span class="link">{l s='Forum' d='Modules.Welcome.Admin'}</span>
              </a>
            </div>
          </div>
          <div class="row">
            <div class="col-md-6 text-center text-md-center link-container">
              <a class="final-link" href="https://www.prestashop.com/en/training-prestashop" target="_blank">
                <div class="training"></div>
                <span class="link">{l s='Training' d='Modules.Welcome.Admin'}</span>
              </a>
            </div>
            <div class="col-md-6 text-center text-md-center link-container">
              <a class="final-link" href="https://www.youtube.com/user/prestashop" target="_blank">
                <div class="video-tutorial"></div>
                <span class="link">{l s='Video tutorial' d='Modules.Welcome.Admin'}</span>
              </a>
            </div>
          </div>
        </div>
    </div>
    <div class="modal-footer">
        <div class="col-12">
            <div class="text-center text-md-center">
                <button class="btn btn-primary onboarding-button-next">{l s='I\'m ready' d='Modules.Welcome.Admin'}</button>
            </div>
        </div>
    </div>
</div>
