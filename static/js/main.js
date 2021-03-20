$(document).ready(() => {
  $('.open-signup').on('click', () => {
    $('#login-modal').css('display', 'none');
    $('#signup-modal').css('display', 'flex');
  });

  $('.open-login').on('click', () => {
    $('#signup-modal').css('display', 'none');
    $('#login-modal').css('display', 'flex');
  });

  $('.modal-close-button').on('click', () => {
    $('#signup-modal').css('display', 'none');
    $('#login-modal').css('display', 'none');
  });
});
