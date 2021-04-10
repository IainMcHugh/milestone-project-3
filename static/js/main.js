$(document).ready(() => {
  $('.hamburger-button').on('click', () => {
    $('.mobile-menu').css('display', 'flex');
  });

  $('.open-signup').on('click', () => {
    $('#login-modal').css('display', 'none');
    $('#signup-modal').css('display', 'flex');
    $('.mobile-menu').css('display', 'none');
  });

  $('.open-login').on('click', () => {
    $('#signup-modal').css('display', 'none');
    $('#login-modal').css('display', 'flex');
    $('.mobile-menu').css('display', 'none');
  });

  $('.close-button').on('click', () => {
    $('#signup-modal').css('display', 'none');
    $('#login-modal').css('display', 'none');
    $('.mobile-menu').css('display', 'none');
  });
});
