let calendarShow =1;
function settingDate(date,day)
{
    date = new Date(date);
    date.setDate(day); //sets the numeric date for the given 
    date.setHours(23);//we want to display the date and the hour of the current time
    return date;
}

function getDateBetween(date1,date2)
{
    let range1 = new Date(date1); 
    //converting the string into the numeric type
    let range2 = new Date(date2);
    date1=settingDate(date1, 31); //setting the date from the month till date 31 if not it will display the other month
    date2=settingDate(date2, 31);
 //now to get the end date for the each month 
 let temp;
 let dates=[];
    while(date1<=date2){
        //for the loop to br runned till the specified date
       if(date1.getDate()!=31)
       {
           temp=settingDate(date1,0); //here what happens is , when the above condition is met, the date is changed and increased for the next
       
        if(temp>=range1 && temp<=range2) dates.push(temp);  
            date1= settingDate(date1,31);  
        //here the dates for the month gets changed 
       }
        else{
             //now for the month 
             temp=new Date(date1);
             if(temp>=range1 && temp<=range2) dates.push(temp);
             date1.setMonth(date1.getMonth() + 1);
        }
       
    }
    //console.log(dates);
    let content="<div class = 'calendarButns'><button id = 'calendarPrev'onclick='callPrev()' disabled > Past </button>  <button id = 'calendarNext'onclick='callNext()'> Future </button> </div>"; // Since we want the button at the top of our page
    let weekDays =[
                    {shortDay:'Mon' , fullDay:'Monday'},
                    {shortDay:'Tue' , fullDay:'Tuesday'},
                    {shortDay:'Wed' , fullDay:'Wednesday'},
                    {shortDay:'Thur' , fullDay:'Thursday'},
                    {shortDay:'Fri' ,  fullDay:'Friday'},
                    {shortDay:'Sat' , fullDay:'Saturday'},
                    {shortDay:'Sun' , fullDay:'Sunday'}
                   ];
    let lastDate, firstDate; //to store the first and last date of the each month
    for(let i=0; i<dates.length; i++){
        lastDate= dates[i]; //it returns the last date of the index
        firstDate= new Date(dates[i].getFullYear(),dates[i].getMonth(),1); // format 2020-01-01 returns the first date
        content += "<div id='calendarTable_" + (i + 1) + "' class='calendarDiv'>";
                content +=
                        "<h2>" +
                        firstDate.toString().split(" ")[1] +
                        "-" +
                        firstDate.getFullYear() +
                        "</h2>"     ;             //it helps us to get the format "Feb - 2020 "
            
            content+= "<table class ='calendarTable'>";
                content+= "<thead >";
                weekDays.map(item=>{
                    content += "<th>"+ item.fullDay+"</th>";
                });
                content+="</thead>";
                    content += "<tbody>";
                       let j=1;  //here we print the dates in the calendar body
                        let displayNum;
                        while(j <= lastDate.getDate()){
                            //we display the dates in the row
                            content+="<tr>";
                                for(let k = 0; k < 7; k ++) //since we have seven days in the week we ned to display till seven days
                                {
                                    displayNum =j < 10 ?"0" +j :j; // the way our dates will be displayed
                                    if(j==1){
                                            if(firstDate.toString().split(" ")[0] == weekDays[k].shortDay)
                                            {
                                                content += "<td>" + displayNum + "</td>";
                                                j++;
                                            }
                                            else{
                                                content+= "<td></td>";  // we display the blank
                                            }
                                        }
                                        else if(j> lastDate.getDate())
                                        {
                                            content+= "<td></td>";
                                        }
                                            else{
                                                content += "<td>" + displayNum + "</td>";
                                                j++;
                                            }
                                }
                            content +="</tr>";

                        }
                    content += "</tbody>";
            content+="</table>";
        content +="</div>";
    }
    return content;
}
    function callNext()   //for moving the calendar to the next month . since if we go front we need to come back so we have used the prev in the front 
    {
        let alltable=document.getElementsByClassName('calendarDiv');
        document.getElementById('calendarPrev').disabled=false;
        calendarShow++;
        if(calendarShow<=alltable.length)
        {
            for(let i = 0; i<alltable.length;i++)
        {
            alltable[i].style.display="none";
        }
        document.getElementById('calendarTable_'+calendarShow).style.display="block";
        if(calendarShow == alltable.length)
        {
            document.getElementById("calendarNext").disabled=true;
        }
       }
    }
    function callPrev()
    {
        let alltable=document.getElementsByClassName('calendarDiv'); // calling the class for displaying the content 
        document.getElementById('calendarNext').disabled=false;
        calendarShow --;
        if(calendarShow >= 1)
        {
            for(let i = 0; i< alltable.length; i++)
        {
            alltable[i].style.display="none";
        }
        document.getElementById('calendarTable_'+calendarShow).style.display="block";
        if(calendarShow == 1)
        {
            document.getElementById("calendarPrev").disabled=true;
        }
        
        }
    }

//starting portion of the code
let content = getDateBetween("2020/01/01", "2020/10/01"); //helps us to get the date between the starting and the ending .
document.getElementById("calendar").innerHTML = content;
 //we are calling the html portion and wanting it to be displayed as the content of the page