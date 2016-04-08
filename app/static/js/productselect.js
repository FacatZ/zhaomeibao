$(document).ready(function(){
  var lg = new LG.URL(window.location.href);

  // -------fenlei---------
  var fenleilist = lg.get("fenlei");
  if( fenleilist != undefined ){
    for(var i=0; i<fenleilist.length;i++){
      var id = fenleilist[i];
      $(".tableBody[name='fenlei']").children("#"+id).addClass("darkBackground");
    }
  }else{
    $(".tableBody[name='fenlei']").children().eq(0).addClass("darkBackground");
  }

  // ---------chandi-----------
  var chandilist = lg.get("chandi");
  if( chandilist != undefined ){
    for(var i=0; i<chandilist.length;i++){
      var id = chandilist[i];
      $(".tableBody[name='chandi']").children("#"+id).addClass("darkBackground");
    }
  }else{
    $(".tableBody[name='chandi']").children().eq(0).addClass("darkBackground");
  }

  // ---------jiaogedi--------
  var jiaogedilist = lg.get("jiaogedi");
  if( jiaogedilist != undefined ){
    for(var i=0; i<jiaogedilist.length;i++){
      var id = jiaogedilist[i];
      $(".tableBody[name='jiaogedi']").children("#"+id).addClass("darkBackground");
    }
  }else{
    $(".tableBody[name='jiaogedi']").children().eq(0).addClass("darkBackground");
  }

  // --------Qnet---------
  var Qnetlist = lg.get("Qnet");
  if( Qnetlist != undefined ){
    for(var i=0; i<Qnetlist.length;i++){
      var id = Qnetlist[i];
      $(".tableBody[name='Qnet']").children("#"+id).addClass("darkBackground");
    }
  }else{
    $(".tableBody[name='Qnet']").children().eq(0).addClass("darkBackground");
  }
  // ------St--------
  var Stlist = lg.get("St");
  if( Stlist != undefined ){
    for(var i=0; i<Stlist.length;i++){
      var id = Stlist[i];
      $(".tableBody[name='St']").children("#"+id).addClass("darkBackground");
    }
  }else{
    $(".tableBody[name='St']").children().eq(0).addClass("darkBackground");
  }
  // ------V--------
  var Vlist = lg.get("V");
  if( Vlist != undefined ){
    for(var i=0; i<Vlist.length;i++){
      var id = Vlist[i];
      $(".tableBody[name='V']").children("#"+id).addClass("darkBackground");
    }
  }else{
    $(".tableBody[name='V']").children().eq(0).addClass("darkBackground");
  }
  // ------Mt--------
  var Mt = lg.get("Mt");
  if( Mt != undefined ){
    for(var i=0; i<Mt.length;i++){
      var id = Mt[i];
      $(".tableBody[name='Mt']").children("#"+id).addClass("darkBackground");
    }
  }else{
    $(".tableBody[name='Mt']").children().eq(0).addClass("darkBackground");
  }



  $(".tableBox").click(function(){
    var $this = $(this);
    var tdname = $this.parent().attr("name");
    var boxString = $this.html();
    
    if(boxString == "不限"){
      $this.nextAll().removeClass("darkBackground");
      lg.remove(tdname);
      lg.jump();
      if( !$this.hasClass("darkBackground")){
        $this.addClass("darkBackground");
      }

    }else{
      var val = $this.attr("id");
  		if($this.hasClass("darkBackground")){
  			$this.removeClass("darkBackground");

        lg.removeVal(tdname, val);
  			
        if( $this.siblings().filter(".darkBackground").length < 1) {
  				$this.prevAll().eq(-1).addClass("darkBackground");
          lg.remove(tdname);
        }
        lg.jump();
  		}else{
	  		$this.addClass("darkBackground");
  			$this.prevAll().eq(-1).removeClass("darkBackground");
        lg.add(tdname, val);
        lg.jump();
  		}
  	}
  });
  
});


var LG=(function(lg){
    var objURL=function(url){
        this.ourl=url||window.location.href;
        this.href="";//?前面部分
        this.params={};//url参数对象
        this.jing="";//#及后面部分
        this.init();
    }
    //分析url,得到?前面存入this.href,参数解析为this.params对象，#号及后面存入this.jing
    objURL.prototype.init=function(){
        var str=this.ourl;
        var index=str.indexOf("#");
        if(index>0){
            this.jing=str.substr(index);
            str=str.substring(0,index);
        }
        index=str.indexOf("?");
        if(index>0){
          this.href=str.substring(0,index);
          str=str.substr(index+1);
          var parts=str.split("&");
          for(var i=0;i<parts.length;i++){
            var kv=parts[i].split("=");
            var kv2=kv[1].split(",");
            for(var j=0;j<kv2.length;j++){
              if( this.params[kv[0]]==undefined){
                this.params[kv[0]] = [];
              }
              if( this.params[kv[0]].indexOf(kv2[j]) == -1 ){
                this.params[kv[0]].push(kv2[j]);
              }
            }
          }
        }
        else{
            this.href=this.ourl;
            this.params={};
        }
    }
    //只是修改this.params
    objURL.prototype.set=function(key,val){
      if(this.params[key] == undefined){
        this.params[key] = [];
      }
        this.params[key].push(val);
    }
    objURL.prototype.add=function(key, val){
      if(this.params[key] == undefined){
        this.params[key] = [];
      }
      this.params[key].push(val);
    }
    //只是设置this.params
    objURL.prototype.remove=function(key){
        this.params[key]=undefined;
    }
    objURL.prototype.removeVal=function(key, val){
      var index=this.params[key].indexOf(val);
      if(index > -1){
        this.params[key].splice(index, 1);
      }
    }
    //根据三部分组成操作后的url
    objURL.prototype.url=function(){
        var strurl=this.href;
        var objps=[];//这里用数组组织,再做join操作
        for(var k in this.params){
            if(this.params[k]){
              // alert(this.params[k].join("|"));
                objps.push(k+"="+this.params[k]);
            }

        }
        if(objps.length>0){
            strurl+="?"+objps.join("&");
        }
        if(this.jing.length>0){
            strurl+=this.jing;
        }
        return strurl;
    }
    //得到参数值
    objURL.prototype.get=function(key){
        return this.params[key];
    }    
    objURL.prototype.jump=function(){
        window.location.href = this.url();
    }
    lg.URL=objURL;
    return lg;
}(LG||{}));