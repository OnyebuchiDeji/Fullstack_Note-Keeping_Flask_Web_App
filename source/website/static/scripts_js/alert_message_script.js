function closeAlertMessage()
{
    alertMessages = document.getElementsByClassName("alert_message");

    for (i = 0; i < alertMessages.length; i++)
    {
        alertMessages[i].remove();
        // alertMessages[i].innerHTML = "";
        // alertMessages[i].style="";
        // alertMessages[i].style.color = "";
        // alertMessages[i].style.backgroundColor = "black";
        // alertMessages[i].style.border = "";
        // document.removeChild(alertMessages[i]);
        // alertMessages[i].ariaHidden = true;
    }
    console.log("Closed Alert Message!");
}

function closeAlertMessageHook()
{
    close_btns = document.getElementsByClassName("close_alert_message");
    for (i = 0; i < close_btns.length; i++)
    {
        close_btns[i].onclick = closeAlertMessage;
        // close_btns[i].onclick = function(){alert("Clicked!")};

    }

    /// NOTE CANNOT DO THIS FOR NON-ASSOCIATIVE ARRAYS IN JS
    /**
     * 
     
    for (btn in close_btns)
    {
        // btn.onClick = closeAlertMessage;
        // close_btns[i].onclick = function(){alert("Clicked!")};
        btn.onclick = function(){alert("Clicked!")};
    }
    */
}



function main()
{
    closeAlertMessageHook()
}


main()