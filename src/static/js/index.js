
function getMessages_success(data){
    msgs=parseMessage(data);
    for (var i = 0; i < msgs.length; i++){

        var personal=msgs[i].area+" "+msgs[i].school+" "+msgs[i].major+" "+msgs[i].create_time;
        var p_personal="<p class='personal'>"+personal+"</p>";
        var p_center="<p class='center'>"+msgs[i].content+"</p>";
        var div="<div class='message_box'>"+p_personal+p_center+"</div>"
        var li="<li>"+div+"</li>"

        //向ul元素中添加元素
        $("#message_list").append(li);
    }
}

function getMessages(){
    //jquery ajax请求
    $.ajax({
        url: "/api/get_messages",
        type: 'GET',
        dataType: 'json',
        success: getMessages_success
    });
}
//
//页面创建的函数
function createPage() {
    getMessages();
}
//解析get_message返回的json数据
function parseMessage(data){

    //解析json
    var messages=data.messages;
    return messages;
}

createPage()