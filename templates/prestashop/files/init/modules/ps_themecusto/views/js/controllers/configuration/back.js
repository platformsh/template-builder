/**
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
*
* Don't forget to prefix your containers with your own identifier
* to avoid any conflicts with others containers.
*/

$(document).ready(function() {
    $(document).on('click', '#psthemecusto .js-wireframe div, #psthemecusto .js-module-name', function(){
        if ($(this).hasClass('active')) {
            resetActiveCategory();
            $(this).removeClass('active');
        } else {
            resetActiveCategory();
            setActiveCategory($(this));
            $(this).addClass('active');
        }
    });

    $(document).on('click', '#psthemecusto button', function(event) {
        event.preventDefault();
        let action = $(this).parent('div').data('action');
        let name = $(this).parent('div').data('module_name');
        let displayName = $(this).parent('div').data('module_displayname');
        let url = $(this).parent('div').prop('action');
        let id_module = $('.src_parent_'+name).data('id_module');

        if (action == 'uninstall' || action == 'disable' || action == 'reset') {
            $('.modal .action_available').hide();
            $('.modal .'+action).show();
            $('.modal .modal-footer a').prop('href', url).attr('data-name', name).attr('data-action', action);
            $('.modal .module-displayname').html(displayName);
        } else {
            ajaxActionModule(action, id_module, name);
        }
    });

    $(document).on('click', '.modal .modal-footer a', function(event) {
        event.preventDefault();
        let name = $(this).attr('data-name');
        let action = $(this).attr('data-action');
        let id_module = $('.src_parent_'+name).data('id_module');
        ajaxActionModule(action, id_module, name);
    });

    $("#psthemecusto .js-wireframe div").hover(
        function() {
            $(this).find('.on-element').removeClass('displaynone');
            $(this).find('.out-element').addClass('displaynone');
        }, function() {
            $(this).find('.on-element').addClass('displaynone');
            $(this).find('.out-element').removeClass('displaynone');
        }
    );

});

function resetActiveCategory()
{
    $('#psthemecusto .js-wireframe div').removeClass('active');
    $('#psthemecusto .js-wireframe div .on-element').addClass('displaynone');
    $('#psthemecusto .js-wireframe div .out-element').removeClass('displaynone');
    $('#psthemecusto .js-module-name').removeClass('active');
    $('#psthemecusto .js-module-name').parent('.configuration-rectangle').removeClass('active');
    $('#psthemecusto .js-module-name').parent('.configuration-rectangle').find('.module-informations').slideUp();
    $('#psthemecusto .configuration-rectangle-caret .material-icons.up').hide();
    $('#psthemecusto .configuration-rectangle-caret .material-icons.down').show();
}

function setActiveCategory(elem)
{
    let module = elem.data('module_name');
    $('.js-img-'+module).addClass('active');
    $('.js-img-'+module+' .on-element').removeClass('displaynone');
    $('.js-img-'+module+' .out-element').addClass('displaynone');
    $('.js-title-'+module).addClass('active');
    $('.js-title-'+module).parent('.configuration-rectangle').addClass('active');
    $('.js-title-'+module).parent('.configuration-rectangle').find('.module-informations').slideDown();
    $('.js-title-'+module+' .material-icons.up').show();
    $('.js-title-'+module+' .material-icons.down').hide();

    headHeight = $('.page-head.with-tabs').height();
    navHeight = $('#header_infos').height();
    topOffset = headHeight + navHeight;
    if (elem.hasClass('js-img-'+module)) {
        $('html, body').animate({scrollTop: $('.js-title-'+module).offset().top-topOffset}, 1000);
    } else {
        if ($(window).innerWidth() > 991) {
            $('html, body').animate({scrollTop: $('.js-img-'+module).offset().top-topOffset}, 1000);
        }
    }
}

function ajaxActionModule(action, id_module, name)
{
    if (typeof action != "undefined"
    && typeof id_module != "undefined"
    && typeof name != "undefined") {
        $.ajax({
            type: 'POST',
            url: admin_module_ajax_url_psthemecusto,
            data: {
                ajax : true,
                action : 'UpdateModule',
                id_module : id_module,
                module_name : name,
                action_module : action
            },
            beforeSend : function(data) {
                $('.src_loader_'+name).show();
                $('.src_parent_'+name).hide();
            },
            success : function(data) {
                $('.src_parent_'+name).html(data);
                $.growl.notice({ title: "Notice!", message: module_action_sucess});
                $('.src_loader_'+name).hide();
                $('.src_parent_'+name).show();
            },
            error : function(data) {
                $('.src_loader_'+name).hide();
                $('.src_parent_'+name).show();
                $.growl.error({ title: "Notice!", message: module_action_failed });
            }
        });
    }
}