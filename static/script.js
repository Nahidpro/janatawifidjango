document.getElementById("p2").style.color = "red";

var editstate = null;

var editbutton = document.getElementById('editbutton')


editbutton.addEventListener('click', (e)=> console.log('ggggggggggg'))

 let abf =(datee,trade_code,high,low,open,close)=> {
    var date = new Date(datee).toISOString().slice(0, 10);
    editstate={date,trade_code,high,low,open,close}
    document.getElementById("date").value = editstate.date;
    document.getElementById("trade_code").value = editstate.trade_code;
    document.getElementById("high").value = editstate.high;
    document.getElementById("low").value = editstate.low;
    document.getElementById("open").value = editstate.open;
    document.getElementById("close").value = editstate.close;
    

    


    
}