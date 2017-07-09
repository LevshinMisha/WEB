function getCookie(name)
{
  var matches = document.cookie.match(new RegExp("(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}

function setCookie(name, value)
{
    document.cookie = name + '=' + value + '; path=/;';
    checks();
}

function showHelp()
{
    $('#help')[0].style.display = 'block';
}

function hideHelp()
{
    $('#help')[0].style.display = 'none';
}

function createElement(type, className, innerText)
{
    var element = document.createElement(type);
    element.className = className;
    element.innerText = innerText;
    return element
}

setCookie('screen', window.screen.width + ' x ' + window.screen.height);

function main()
{
    var help = $('#help')[0];
    if (help !== null)
    {
        help.style.display = 'none';
        help.style.whiteSpace = 'pre-wrap';
        help.innerHTML = 'Нажмите F1, чтобы открыть\\закрыть хелп\nНажимайте на миниатюру чтобы увидеть полную картинку\nПеремещение по галерее с помощью стрелок\nESC - закрывает картинку';
    }
    if (document.getElementById('gallery') !== null)
    {
        setInterval(getLikes, 2000);
        setInterval(getComments, 10000);
        setInterval(locationCheck, 100);
    }
}

$(main);