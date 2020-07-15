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

<div class="onboarding-advancement" style="display: none">
  <div class="advancement-groups">
    {foreach from=$steps.groups item=group key=k}
      <div class="group group-{$k}" style="width: {math equation="(x / y) * 100" x=$group.steps|@count y=$totalSteps}%;">
        <div class="advancement" style="width: {$percent_real}%;"></div>
        <div class="id">{$k+1}</div>
      </div>
    {/foreach}
  </div>
  <div class="col-md-8">
    <h4 class="group-title"></h4>
    <div class="step-title step-title-1"></div>
    <div class="step-title step-title-2"></div>
  </div>
  <button class="btn btn-primary onboarding-button-next">{l s='Continue' d='Modules.Welcome.Admin'}</button>
  <a class="onboarding-button-shut-down">{l s='Skip this tutorial' d='Modules.Welcome.Admin'}</a>
</div>

<script type="text/javascript">

  var onBoarding;

  $(function(){
    onBoarding = new OnBoarding({$currentStep}, {$jsonSteps nofilter}, {$isShutDown}, "{$link}", baseAdminDir);

    {foreach from=$templates item=template}
      onBoarding.addTemplate('{$template['name']}', '{$template['content']}');
    {/foreach}

    onBoarding.showCurrentStep();

    var body = $("body");

    body.delegate(".onboarding-button-next", "click", function(){
      if ($(this).is('.with-spinner')) {
        if (!$(this).is('.animated')) {
          $(this).addClass('animated');
          onBoarding.gotoNextStep();
        }
      } else {
        onBoarding.gotoNextStep();
      }
    }).delegate(".onboarding-button-shut-down", "click", function(){
      onBoarding.setShutDown(true);
    }).delegate(".onboarding-button-resume", "click", function(){
      onBoarding.setShutDown(false);
    }).delegate(".onboarding-button-goto-current", "click", function(){
      onBoarding.gotoLastSavePoint();
    }).delegate(".onboarding-button-stop", "click", function(){
      onBoarding.stop();
    });

  });

</script>
