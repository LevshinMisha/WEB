function getCookie(name)
{
  var matches = document.cookie.match(new RegExp("(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}


function getHelpElement()
{
    return document.getElementById('help')
}


function showHelp()
{
    getHelpElement().style.display = 'block';
}

function hideHelp()
{
    getHelpElement().style.display = 'none';
}

window.onload = function (event)
{
    console.log(document.cookie);
    if (getCookie('big_img') !== undefined)
    {
        document.body.style.backgroundImage = 'url(' + getCookie('big_img') + ')';
    }
    try
    {
        getHelpElement().style.display = 'none';
        getHelpElement().style.whiteSpace = 'pre-wrap';
        getHelpElement().innerHTML = 'Нажмите F1, чтобы открыть\\закрыть хелп\nНажимайте на миниатюру чтобы увидеть полную картинку\nПеремещение по галерее с помощью стрелок\nESC - закрывает картинку';
        cookieChange();

    }
    catch (Exception)
    {

    }
}