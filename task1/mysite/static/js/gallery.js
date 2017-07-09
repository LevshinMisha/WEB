IMAGE_COUNT = 19;
IMG_DICT = {};
CURRENT_COMMENTS = [];
CURRENT_LIKES = '';
CURRENT_ID = '';

function pre_download_next_and_prev_image(id)
{
    var int_id = parseInt(id);
    if (int_id !== 0)
        addImageInCash(getImageSrc((int_id - 1).toString()));
    else
        addImageInCash(getImageSrc((IMAGE_COUNT - 1).toString()));
    if (int_id !== IMAGE_COUNT)
        addImageInCash(getImageSrc((int_id + 1).toString()));
    else
        addImageInCash(getImageSrc('0'));
}

function closeBigImage()
{
    setCookie('img', '-1');
    CURRENT_ID = '-1';
    document.location = '#-1';
}

document.body.onkeydown = function (e)
{
    if (e.keyCode === 112)
    {
        e.preventDefault();
        e.stopImmediatePropagation();
        if ($('#help')[0].style.display === 'none')
            showHelp();
        else
            hideHelp();
    }
    if (getCookie('img') !== '-1' && getCookie('img') !== undefined)
    {
        if (e.keyCode === 27)
        {
            closeBigImage();
        }
        if (e.keyCode === 37)
        {
            var c = parseInt(getCookie('img')) - 1;
            if (c < 0)
                c = IMAGE_COUNT;
            expandImage(c.toString());
        }
        if (e.keyCode === 39)
        {
            var c = parseInt(getCookie('img')) + 1;
            if (c === IMAGE_COUNT + 1)
                c = 0;
            expandImage(c.toString());
        }
    }
};

function getImageSrc(id)
{
    var src_parts = $('#'+id)[0].src.split('/');
    var src = '';
    for (var i = 0; i < src_parts.length; i++)
    {
        if (src_parts[i] !== 'thumbnails')
        {
            if (i !== src_parts.length - 1)
                src += src_parts[i] + '/';
            else
                src += src_parts[i].slice(0, -7) + '.jpg';
        }
    }
    return src;
}

function expandImage(id)
{
    CURRENT_COMMENTS = [];
    CURRENT_LIKES = '';
    if (CURRENT_ID !== id && CURRENT_ID !== -1)
    {
        clearComments();
        CURRENT_ID = id;
        document.location = '#' + id;
        $('#comments')[0].innerHTML = '<div class="comment" style="padding: 5px 0; width:90vw">Loading...</div>';
        $('#like_button')[0].innerText= "Лайки не загрузились";
        document.cookie = 'img=' + id + '; path=/;';
        $('#gallery_big_img')[0].style.opacity = 0.7;
        var src = getImageSrc(id);

        addImageInCash(src);
        pre_download_next_and_prev_image(id);

        var gallery_big_img_container = $('#gallery_big_img_container')[0];
        if (gallery_big_img_container.style.display !== 'flex')
            gallery_big_img_container.style.display = 'flex';

        $('#button_make_img_background')[0].onclick = makeBackgroundImage(src);
        if (IMG_DICT[src] !== 'loaded') // Этот костыль я посвещаю работе атрибута src в firefox.
        {
            $('#gallery_big_img')[0].src = "";
            window.setTimeout(function()
            {
                $('#gallery_big_img')[0].src = src;
            }, 50)
        }
        else
            $('#gallery_big_img')[0].src = src;
        window.setTimeout(function() { getComments(); getLikes(); }, 500)
    }
}

function imgOnClick(id)
{
    setCookie('img', id.toString());
}

function bigImgOnLoad(id)
{
    $('#gallery_big_img')[0].style.opacity = 1;
}

function makeBackgroundImage(url)
{
    return function (event) { setCookie('big_img', url); }
}

function addImageInCash(src)
{
    if (!IMG_DICT[src])
    {
        IMG_DICT[src] = 'loading';
        var image = new Image();
        image.src = src;
        console.log(src + ' Загружается');
        image.onload = function()
        {
            console.log(src + ' Загружено');
            IMG_DICT[src] = 'loaded';
        };
        $('#gallery_cash').append(image);
    }
}

function ajax(url, onComplete)
{
    $.get(url).done(onComplete).fail(function(xhr, status, errorText) { console.log(errorText) });
}

function isCommentsNeedToUpdate(comments)
{
    if (comments.length !== CURRENT_COMMENTS.length)
        return true;
    for(var i = 0; i < comments.length; i++)
        if (comments[i].author !== CURRENT_COMMENTS[i].author || comments[i].text !== CURRENT_COMMENTS[i].text)
            return true;
    return false
}

function clearComments()
{
    $('#comments')[0].innerHTML = '';
}

function getComments()
{
    function afterResponse(responseText)
    {
        var comments = JSON.parse(responseText);
        if (isCommentsNeedToUpdate(comments.comments))
        {
            CURRENT_COMMENTS = comments.comments;
            clearComments();
            for (var i = 0; i < comments.comments.length; i++)
            {
                var comment = createElement('div', 'comment', '');
                comment.appendChild(createElement('div', 'comment_author', comments.comments[i].author));
                comment.appendChild(createElement('div', 'comment_text', comments.comments[i].text));
                $('#comments').append(comment)
            }
        }
        else
            if (CURRENT_COMMENTS.length === 0) clearComments();
    }

    var picture = getCookie('img');
    if (picture !== '-1') ajax('getComments/' + picture, afterResponse)
}

function addComment()
{
    function afterResponse(responseText)
    {
        alert(responseText);
        getComments();
    }

    function changeSymbol(symbol, newSymbol, text)
    {
        var s = '';
        for (var i in text.split(symbol))
            s += text.split(symbol)[i] + newSymbol;
        return s.slice(0, s.length - 2)
    }

    var picture = getCookie('img');
    var text = $('#new_comment_text')[0].value;
    console.log(text);
    text = 'addComment/' + picture + '/' + text.replace('?', ' \\q');

    text = changeSymbol('?', ' \\q', text);
    text = changeSymbol('\n', ' \\n', text);
    console.log(text);
    ajax(text, afterResponse)
}

function like()
{
    function afterResponse(responseText)
    {
        getLikes()
    }

    var picture = getCookie('img');
    ajax('like/' + picture, afterResponse)
}

function getLikes()
{
    function afterResponse(responseText)
    {
        if (responseText !== CURRENT_LIKES)
        {
            CURRENT_LIKES = responseText;
            $('#like_button')[0].innerText= "Лайков:" + responseText;
        }
    }

    var picture = getCookie('img');
    if (picture !== '-1')
        ajax('getLikes/' + picture, afterResponse)
}

function downloadXls()
{
    window.location = 'xls';
}

function locationCheck()
{
    if (document.location.hash === '#-1')
    {
        if (CURRENT_ID !== '-1')
            closeBigImage()
    }
    else if (document.location.hash !== '')
        expandImage(document.location.hash.slice(1, document.location.length))
}

function galleryCheck()
{
    if ($('#gallery')[0] !== null)
    {
        if (getCookie('img') === '-1' || getCookie('img') === undefined)
        {
            $('#gallery_big_img_container')[0].style.display = 'none';
            document.location = '#-1';
        }
        else
        {
            expandImage(getCookie('img'));
        }
    }
}

function bigImgCheck()
{
    if (getCookie('big_img') !== undefined)
    {
        var background = $('#background')[0];
        background.style.backgroundImage = 'url(' + getCookie('big_img') + ')';
        background.style.display = "block";
    }
}

function checks()
{
    galleryCheck();
    bigImgCheck();
}

$(checks);