function ajax(url, func)
{
    var xhr = new XMLHttpRequest();

    xhr.open('GET', url, true);
    xhr.send();
    xhr.onreadystatechange = function()
    {
        if (xhr.readyState != 4) return;
        if (xhr.status != 200)
        {
            alert(xhr.status + ': ' + xhr.statusText);
        }
        else
        {
            func(xhr.responseText);
        }
    }
}


function makeChoice(codeNameNextStage)
{
    function afterResponse(response)
    {
        if (response === 'Читерок')
            return
        r = JSON.parse(response);
        document.getElementById('img').src = r.img;
        document.getElementById('text').innerHTML = r.text;
        setChoices(r.choices);
    }

    ajax('nextStage/' + codeNameNextStage, afterResponse);
}

function setChoices(choices)
{
    document.getElementById('choices').innerHTML = '';
    choices.forEach(function(choice)
    {
        d = document.createElement('div');
        d.classList.add('choice', 'menu-item');
        d.title = choice.title;
        d.onclick = function() {makeChoice(choice.stage_to)};
        d.innerText = choice.text;
        document.getElementById('choices').appendChild(d);
    })
}


