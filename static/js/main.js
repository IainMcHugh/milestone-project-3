$(document).ready(() => {
  $('.hamburger-button').on('click', () => {
    $('.mobile-menu').css('display', 'flex');
  });

  $('.open-signup').on('click', () => {
    $('#signup-modal').css('display', 'flex');
    $('#login-modal').css('display', 'none');
    $('.mobile-menu').css('display', 'none');
    $('#info-modal').css('display', 'none');
  });

  $('.open-login').on('click', () => {
    $('#login-modal').css('display', 'flex');
    $('#signup-modal').css('display', 'none');
    $('.mobile-menu').css('display', 'none');
    $('#info-modal').css('display', 'none');
  });

  $('.open-info').on('click', () => {
    $('#info-modal').css('display', 'flex');
    $('#signup-modal').css('display', 'none');
    $('#login-modal').css('display', 'none');
    $('.mobile-menu').css('display', 'none');
  });

  $('.close-button').on('click', () => {
    $('#signup-modal').css('display', 'none');
    $('#login-modal').css('display', 'none');
    $('.mobile-menu').css('display', 'none');
    $('#info-modal').css('display', 'none');
  });
});
