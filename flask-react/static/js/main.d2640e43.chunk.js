(window.webpackJsonp=window.webpackJsonp||[]).push([[0],{33:function(e,t,n){e.exports=n(70)},38:function(e,t,n){},40:function(e,t,n){},67:function(e,t){},70:function(e,t,n){"use strict";n.r(t);var a=n(0),s=n.n(a),o=n(31),r=n.n(o),u=(n(38),n(3)),i=n(4),c=n(6),m=n(5),l=n(7),p=(n(40),function(e){function t(e){var n;return Object(u.a)(this,t),(n=Object(c.a)(this,Object(m.a)(t).call(this,e))).submitForm=function(e){e.preventDefault(),console.log("Form Submitted")},n.inputChange=function(e){n.props.updateUsername(e.target.value)},n.textUsername=s.a.createRef(),n}return Object(l.a)(t,e),Object(i.a)(t,[{key:"render",value:function(){var e=this;return s.a.createElement("form",{onSubmit:this.submitForm},s.a.createElement("input",{type:"text",name:"username",onChange:function(t){return e.inputChange(t)}}),s.a.createElement("input",{type:"text",name:"password"}),s.a.createElement("button",null,"Submit"))}}]),t}(s.a.Component)),d=n(32),h=n.n(d),f=function(e){function t(e){var n;return Object(u.a)(this,t),(n=Object(c.a)(this,Object(m.a)(t).call(this,e))).connectToFlask=function(){n.socket.emit("create",n.props.username)},n.updateMessage=function(e){console.log(e),n.setState({message:JSON.stringify(e)})},n.socket=h()("http://localhost:5000"),n.state={message:""},n}return Object(l.a)(t,e),Object(i.a)(t,[{key:"componentWillMount",value:function(){this.socket.on("join_room",function(e){alert(JSON.stringify(e)),this.updateMessage(JSON.stringify(e))})}},{key:"render",value:function(){return s.a.createElement("div",null,s.a.createElement("h1",null,"Server Response"),s.a.createElement("h2",null,this.props.username),s.a.createElement("button",{onClick:this.connectToFlask},"CONNECT TO FLASK"),s.a.createElement("h2",null,this.state.message))}}]),t}(s.a.Component),g=function(e){function t(e){var n;return Object(u.a)(this,t),(n=Object(c.a)(this,Object(m.a)(t).call(this,e))).updateMessage=function(e){n.setState({message:e})},n.updateUsername=function(e){n.setState({username:e})},n.updatePassword=function(e){n.setState({password:e})},n.state={message:"",username:"",password:""},n}return Object(l.a)(t,e),Object(i.a)(t,[{key:"render",value:function(){return s.a.createElement("div",{className:"App"},s.a.createElement(p,{updateMessage:this.updateMessage,updateUsername:this.updateUsername,updatePassword:this.updatePassword}),s.a.createElement(f,{updateMessage:this.updateMessage,updateUsername:this.updateUsername,updatePassword:this.updatePassword,message:this.state.message,username:this.state.username,password:this.state.password}))}}]),t}(a.Component);Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));r.a.render(s.a.createElement(g,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then(function(e){e.unregister()})}},[[33,2,1]]]);
//# sourceMappingURL=main.d2640e43.chunk.js.map