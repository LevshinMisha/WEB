messages_count = 0;
already_delete = false;
animation_is_over = true;
animation_time = 1000;
messages = [];

function ajax(url, onComplete)
{
    $.get(url).done(onComplete).fail(function(xhr, status, errorText) { alert(errorText) });
}

function addMessageToChat(message)
{
    animation_is_over = false;
    $('#chat').append('<div class="message">' + message + '</div>');
    if (messages_count < 10)
        $('.message:last').fadeIn(animation_time);
    else
        $('.message:last').slideDown(animation_time);
    messages_count++;
    if (messages_count > 10)
        deleteFirstMessage();
    setTimeout(function() { animation_is_over = true;  }, animation_time);
}

function deleteFirstMessage()
{
    if (already_delete)
        $('.message:first').remove();
    already_delete = true;
    $('.message:first').css('height', '50px').css('min-height', '0').slideUp(animation_time);
}

function addMessagesToChat(data)
{
    var m = JSON.parse(data);
    var m1 = [];
    m.forEach(function(item) {
        a = true
        messages.forEach(function(item2) {
            if (item.id === item2.id)
                a = false;

        })
        if (a)
            m1.push(item.text)
    });
    messages = m;
    m1.forEach(addMessageToChat);
}

function getMessages()
{
    if (animation_is_over)
    {
        ajax('messages', addMessagesToChat);
    }
}

function buttonOnClick()
{
    if (animation_is_over)
    {
        var text = $('#text').val();
        ajax('addMessage/' + text, getMessages);
    }
}

function main()
{
    $('button').click(buttonOnClick);
    setInterval(getMessages, 1000);
}

$(main);