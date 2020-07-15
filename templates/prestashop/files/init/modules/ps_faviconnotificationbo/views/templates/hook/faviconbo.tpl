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

<script type="text/javascript">
/*
 * Return total of notification per checkbox checked
 * @param  int nbNewCustomer
 * @param  int nbNewOrder
 * @param  int nbNewMessage
 * @return int result        Total of Notification
 */
function getNotification(nbNewCustomer, nbNewOrder, nbNewMessage) {
    let result = 0;
    //if radiobutton is checked
    {if $bofavicon_params.CHECKBOX_ORDER eq 1} result += nbNewOrder; {/if}
    {if $bofavicon_params.CHECKBOX_CUSTOMER eq 1} result += nbNewCustomer; {/if}
    {if $bofavicon_params.CHECKBOX_MESSAGE eq 1} result += nbNewMessage; {/if}

    return result;
}

function loadAjax(adminController) {
    $.ajax({
        type: 'POST',
        dataType: 'JSON',
        url: adminController,
        data: {
            ajax: true,
            action: "GetNotifications",
        },

        success: function(data) {

            let nbNewCustomers = parseInt(data.customer.total);
            let nbNewOrders = parseInt(data.order.total);
            let nbNewCustomerMessages = parseInt(data.customer_message.total);

            let nbTotalNotification = getNotification(nbNewCustomers, nbNewOrders, nbNewCustomerMessages);

            favicon.badge(nbTotalNotification);
        },
        error: function(err) {
            console.log(err);
            console.log(adminController);
        },
    });
}

function updateNotifications(type) {
  $.post(
    baseAdminDir + "ajax.php",
    {
      "updateElementEmployee": "1",
      "updateElementEmployeeType": type
    }
  );
}

$(document).ready(function() {
    adminController = adminController.replace(/\amp;/g, '');
    //set the configuration of the favicon
    window.favicon = new Favico({
        animation: 'popFade',
        bgColor: BgColor,
        textColor: TxtColor,
    });
    loadAjax(adminController)
    setInterval(function() {
        loadAjax(adminController);
    }, 60000); //refresh notification every 60 seconds

    //update favicon when you click on the customer tab into your backoffice
    $(document).on('click', '#subtab-AdminCustomers', function (e) {
        updateNotifications('customer');
    });
    //update favicon when you click on the customer service tab into your backoffice
    $(document).on('click', '#subtab-AdminCustomerThreads', function (e) {
        updateNotifications('customer_message');
    });
    //update favicon when you click on the order tab into your backoffice
    $(document).on('click', '#subtab-AdminOrders', function (e) {
        updateNotifications('order');
    });
});
</script>
{* Use this if you want to send php var to your js *}
{literal}
<script type="text/javascript">
    let BgColor = "{/literal}{$bofavicon_params.BACKGROUND_COLOR_FAVICONBO|escape:'html':'UTF-8'}{literal}";
    let TxtColor = "{/literal}{$bofavicon_params.TEXT_COLOR_FAVICONBO|escape:'html':'UTF-8'}{literal}";
    let CheckBoxOrder = "{/literal}{$bofavicon_params.CHECKBOX_ORDER|escape:'html':'UTF-8'}{literal}";
    let CheckBoxCustomer = "{/literal}{$bofavicon_params.CHECKBOX_CUSTOMER|escape:'html':'UTF-8'}{literal}";
    let CheckBoxMessage = "{/literal}{$bofavicon_params.CHECKBOX_MESSAGE|escape:'html':'UTF-8'}{literal}";
    let adminController = "{/literal}{$adminController|escape:'htmlall':'UTF-8'}{literal}";
</script>
{/literal}
