messages_count = 0;
already_delete = false;
animation_is_over = true;
animation_time = 1000;
messages = [];

function ajax(url, onComplete)
{
    $.get(url).done(onComplete).fail(function(xhr, status, errorText) { console.log(errorText) });
}

function addMessageToChat(message)
{
    animation_is_over = false;
    $('#chat').append('<div class="message"><div class="text">' + message + '</div></div>');
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
    var first_message = $('.message:first');
    first_message.slideUp(animation_time);
    $('.text:first').slideUp(animation_time);
    setTimeout(function () { first_message.remove() }, animation_time);
}

function addMessagesToChat(data)
{
    var m = JSON.parse(data);
    var m1 = [];
    for (var i = 0; i < m.length; i++)
        {
            var a = true
            for (var j = 0; j < messages.length; j++)
                if (m[i].id === messages[j].id)
                    a = false;
            if (a)
                m1.push(m[i].text)
        }
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

function buttonAddMessageClick()
{
    if (animation_is_over)
    {
        var text = $('#text').val();
        ajax('addMessage/' + text, getMessages);
    }
}

function buttonOnClick()
{
    var id = $(this)[0].id.split(' ');
    $(id[0]).css('background-color', id[1]);
}

function addButtons()
{
    var colors = ['green', 'blue', 'red', 'white', 'orange', 'grey', 'yellow', 'purple'];
    var selectors = ['body', '.text']
    var readable_selectors = ['Цвет фона всего сайта', 'Цвет фона сообщений', '', '', '', '', '']
    selectors.forEach(function(selector) {
        var id = "div-" + selector.replace('.', '');
        $('body').append(readable_selectors[selectors.indexOf(selector)]);
        $('body').append('<div id="'+ id + '"></div>');
        $('#' + id).css('width', '75vw').css('margin', '10px auto')
        colors.forEach(function(color) {
            $('#' + id).append('<button id="' + selector + ' ' + color + '">' + color + '</button>');
        });
    })
    $('button').click(buttonOnClick)
}

function main()
{
    addButtons();
    $('#button').click(buttonAddMessageClick);
    setInterval(getMessages, 1000);
}

$(main);