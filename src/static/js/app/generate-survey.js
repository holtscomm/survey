import $ from 'jquery';

function createSurvey(type, surveyLink) {
  const $email = $('#email');
  const $firstName = $('#firstName');
  const $lastName = $('#lastName');

  if ($email.val() === '' || $firstName.val() === '') {
    alert('One or more of the required fields (email or first name) is empty');
    return false;
  }

  // Emulate a request to the API: don't need to write any new code to make this work!
  $.post('/api/v1/survey/purchase/', {
    'cart_details[0][name]': type,
    email: $email.val(),
    'user_info[first_name]': $firstName.val(),
    'user_info[last_name]': $lastName.val()
  }).done(function (response) {
    const userId = JSON.parse(response).data.user_id;
    $('#doneDiv').html(`
<br /><p class="bg-success">Done: new user id is <a target="_blank" href="/gifts${surveyLink}/?userId=${userId}">${userId}</a>.
<br />A task has been dispatched to send an email to ${$email.val()}.</p>
    `);
  });
}

$('#full').on('click', function () {
  createSurvey('fullform', '');
});
$('#shorta').on('click', function () {
  createSurvey('short_a', '/a');
});
$('#shortb').on('click', function () {
  createSurvey('short_b', '/b');
});
