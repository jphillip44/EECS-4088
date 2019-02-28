(window.webpackJsonp=window.webpackJsonp||[]).push([[0],{40:function(e,t,a){e.exports=a(80)},70:function(e,t){},78:function(e,t,a){},80:function(e,t,a){"use strict";a.r(t);var s=a(0),n=a.n(s),r=a(36),i=a.n(r);Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));var c=a(2),l=a(3),o=a(5),m=a(4),u=a(6),d=a(82),h=a(84),p=a(83),f=function(e){function t(e){var a;return Object(c.a)(this,t),(a=Object(o.a)(this,Object(m.a)(t).call(this,e))).submitUsername=function(e){e.preventDefault(),a.props.socket.emit("joinServer",{username:a.usernameInput.current.value,socketId:a.props.socket.id}),a.usernameInput.current.value=""},a.state={username:"",socketId:""},a.usernameInput=n.a.createRef(),a}return Object(u.a)(t,e),Object(l.a)(t,[{key:"componentDidMount",value:function(){var e=this;this.props.socket.on("games",function(t){e.props.updateGameList(t.games)}),this.props.socket.on("username",function(t){e.props.updateUsername(t),e.props.updateSocketId(e.props.socket.id),e.setState({username:t,socketId:e.props.socket.id}),e.props.history.push("/room")})}},{key:"render",value:function(){return n.a.createElement("div",{className:"hero is-fullheight"},n.a.createElement("div",{className:"hero-body"},n.a.createElement("div",{className:"container has-text-centered"},n.a.createElement("h1",{className:"landing title is-1 has-text-white"},"UI Tester"),n.a.createElement("h5",{className:"subtitle is-5 has-text-light"},"Where dreams go to die"),n.a.createElement("div",{className:"columns is-centered"},n.a.createElement("div",{className:"column is-4"},n.a.createElement("div",{className:"box"},n.a.createElement("form",{onSubmit:this.submitUsername},n.a.createElement("label",{className:"label"},"Pick your username"),n.a.createElement("div",{className:"field"},n.a.createElement("div",{className:"control"},n.a.createElement("input",{className:"input",type:"text",name:"username",placeholder:"Username",maxLength:"10",required:!0,ref:this.usernameInput}))),n.a.createElement("div",{className:"field"},n.a.createElement("div",{className:"control"},n.a.createElement("button",{type:"submit",className:"button is-info is-fullwidth"},"Submit"))))))))))}}]),t}(n.a.Component),g=function(e){function t(){return Object(c.a)(this,t),Object(o.a)(this,Object(m.a)(t).apply(this,arguments))}return Object(u.a)(t,e),Object(l.a)(t,[{key:"render",value:function(){var e,t=this;return e=0!==this.props.gameList.length?this.props.gameList:sessionStorage.getItem("gameList").split(","),n.a.createElement("div",{className:"box"},n.a.createElement("h1",{className:"title"},"Games"),n.a.createElement("div",{className:"content"},n.a.createElement("div",{className:"buttons"},e.map(function(e,a){return n.a.createElement("button",{className:"button",key:a,onClick:function(){return t.props.goToGame(e)}},e)}))))}}]),t}(n.a.Component),v=function(e){function t(e){var a;return Object(c.a)(this,t),(a=Object(o.a)(this,Object(m.a)(t).call(this,e))).sendMessage=function(e){e.preventDefault(),a.props.sendMessage(a.chatInput.current.value),a.chatInput.current.value=""},a.chatInput=n.a.createRef(),a}return Object(u.a)(t,e),Object(l.a)(t,[{key:"render",value:function(){var e=n.a.createElement("ul",{className:"userChatLog has-text-left"},this.props.chatLog.map(function(e,t){return n.a.createElement("li",{key:t},"".concat(e.username,": ").concat(e.message))}));return n.a.createElement("div",{className:"box"},n.a.createElement("h1",{className:"title"},"Chat"),n.a.createElement("div",{className:"content"},e,n.a.createElement("div",{id:"endOfChat"})),n.a.createElement("form",{onSubmit:this.sendMessage},n.a.createElement("div",{className:"field is-grouped"},n.a.createElement("p",{className:"control is-expanded"},n.a.createElement("input",{className:"input",type:"text",name:"chatInput",placeholder:"Type text here",autoComplete:"off",required:!0,ref:this.chatInput})),n.a.createElement("p",{className:"control"},n.a.createElement("button",{className:"button is-info is-fullwidth"},"Submit")))))}}]),t}(n.a.Component),b=function(e){function t(){return Object(c.a)(this,t),Object(o.a)(this,Object(m.a)(t).apply(this,arguments))}return Object(u.a)(t,e),Object(l.a)(t,[{key:"render",value:function(){return n.a.createElement("div",{className:"box"},n.a.createElement("h1",{className:"title"},"Users"),n.a.createElement("div",{className:"content"},n.a.createElement("div",{className:"buttons"},this.props.users.map(function(e,t){return n.a.createElement("span",{className:"button",key:t},e.username)}))))}}]),t}(n.a.Component),E=function(e){function t(e){var a;return Object(c.a)(this,t),(a=Object(o.a)(this,Object(m.a)(t).call(this,e))).onPageRefresh=function(){sessionStorage.setItem("users",JSON.stringify(a.state.users)),sessionStorage.setItem("pageRefreshed","true")},a.afterPageRefresh=function(e){"true"===e&&(console.log("AfterPageRefresh"),sessionStorage.setItem("pageRefreshed","false"),a.props.socket.emit("joinServer",{username:sessionStorage.getItem("username").split("/")[0],socketId:sessionStorage.getItem("socketId")}),a.props.socket.emit("sendToServer",{type:"retrieveUsers"}))},a.sendMessage=function(e){a.props.socket.emit("sendToServer",{type:"chat",username:a.state.username,socketId:a.props.socket.id,message:e})},a.goToGame=function(e){a.props.socket.emit("createGame",e)},a.state={username:"",users:[],chatLog:[]},a}return Object(u.a)(t,e),Object(l.a)(t,[{key:"componentDidMount",value:function(){var e=this;this.props.socket.emit("sendToServer",{type:"retrieveUsers"}),this.props.socket.emit("sendToServer",{type:"retrieveUsername"}),this.props.socket.emit("sendToServer",{type:"chatLog"}),this.props.socket.on("username",function(t){return e.setState({username:t})}),this.props.socket.on("gameStarted",function(t){e.props.history.push("/".concat(t))}),this.props.socket.on("chatLogFromServer",function(t){e.setState({chatLog:t})}),this.props.socket.on("gameOver",function(){console.log("gameover"),e.props.history.push("/room")}),this.props.socket.on("disconnect",function(){console.log("disconnected"),e.props.socket.removeAllListeners(),e.props.history.push("/")}),this.props.socket.on("reconnect",function(){console.log("reconnect"),e.props.socket.emit("joinServer",{username:e.props.userState.username.split("/")[0],socketId:e.props.socket.id}),e.props.socket.emit("sendToServer",{type:"retrieveUsers"})}),this.props.socket.on("userList",function(t){var a,s=Object.keys(t),n=[];for(a=0;a<s.length;a++)n.push({username:t[s[a]],socketId:s[a]});e.setState({users:n})}),this.props.socket.on("userDisconnected",function(t){var a,s=[],n=e.state.users;for(a=0;a<e.state.users.length;a++)n[a].socketId!==t&&s.push(n[a]);e.setState({users:s})}),window.addEventListener("beforeunload",this.onPageRefresh),this.afterPageRefresh(sessionStorage.getItem("pageRefreshed"))}},{key:"render",value:function(){return n.a.createElement("div",{className:"hero is-fullheight"},n.a.createElement("div",{className:"hero-body"},n.a.createElement("div",{className:"container"},n.a.createElement("div",{className:"columns is-centered"},n.a.createElement("div",{className:"column is-6 has-text-centered"},n.a.createElement(g,{gameList:this.props.userState.gameList,goToGame:this.goToGame}),n.a.createElement(v,{sendMessage:this.sendMessage,chatLog:this.state.chatLog,username:this.state.username}),n.a.createElement(b,{users:this.state.users}))))))}}]),t}(n.a.Component),N=function(e){function t(e){var a;return Object(c.a)(this,t),(a=Object(o.a)(this,Object(m.a)(t).call(this,e))).afterPageRefresh=function(e){if("true"===e){console.log("AfterPageRefresh"),sessionStorage.setItem("pageRefreshed","false");var t=JSON.parse(sessionStorage.getItem("state"));a.setState(t)}},a.choosePlayer=function(e){var t;for(t=0;t<a.state.allTargets.length;t++)a.state.allTargets[t].username===e&&a.setState({action:"attack",target:a.state.allTargets[t],showTargets:!1,showSingleTarget:!0})},a.chooseAction=function(e){"attack"===e?a.setState({showTargets:!0}):"defend"!==e&&"reload"!==e||a.setState({action:e,showSingleTarget:!1,target:{}})},a.closeTargetList=function(){a.setState({showTargets:!1})},a.state={allTargets:[],showTargets:!1,showSingleTarget:!1,action:"reload",target:{},player:{}},a}return Object(u.a)(t,e),Object(l.a)(t,[{key:"componentDidMount",value:function(){var e=this;this.props.socket.on("state",function(t){e.setState({target:{},targetList:[],showSingleTarget:!1,showTargets:!1},function(){console.log("state"),console.log(t);var a,s=Object.keys(t),n=[],r={};for(a=0;a<s.length;a++)s[a]===e.props.userState.username?r={username:s[a],hp:t[s[a]].hp,ap:t[s[a]].ap}:"dead"===t[s[a]].hp||n.push({username:s[a],hp:t[s[a]].hp,ap:t[s[a]].ap});"attack"===e.state.action&&0===Object.keys(e.state.target).length&&e.setState({action:"reload"}),0===r.ap?e.setState({allTargets:n,player:r,action:"reload"}):e.setState({allTargets:n,player:r})})}),this.props.socket.on("timerExpired",function(){console.log("timerExpired"),"dead"!==e.state.player.hp&&("attack"===e.state.action&&0===Object.keys(e.state.target).length?(e.props.socket.emit("endOfRound",{target:e.state.target.username,action:"reload",player:e.state.player.username}),e.setState({action:"reload"})):e.props.socket.emit("endOfRound",{target:e.state.target.username,action:e.state.action,player:e.state.player.username}))}),window.addEventListener("beforeunload",function(t){sessionStorage.setItem("state",JSON.stringify(e.state)),sessionStorage.setItem("pageRefreshed","true"),t.returnValue="Refreshing the page will break things"}),this.afterPageRefresh(sessionStorage.getItem("pageRefreshed"))}},{key:"componentWillUnmount",value:function(){this.props.socket.removeAllListeners()}},{key:"render",value:function(){var e=this;return n.a.createElement("div",{className:"hero is-fullheight"},n.a.createElement("div",{className:"hero-body"},n.a.createElement("div",{className:"container has-text-centered"},n.a.createElement("div",{className:"columns is-centered"},n.a.createElement("div",{className:"column is-5"},n.a.createElement("h1",{className:"title is-1 has-text-white"},"007"),n.a.createElement("div",{className:this.state.showSingleTarget?"box":"box is-hidden"},n.a.createElement("h5",{className:"title is-5"},"Target"),n.a.createElement("p",null,this.state.target.username)),n.a.createElement("div",{className:"box"},n.a.createElement("h5",{className:"title is-5"},sessionStorage.getItem("username")),n.a.createElement("div",{className:"level"},n.a.createElement("div",{className:"level-item"},n.a.createElement("span",{className:"button is-white"},"HP: ",this.state.player.hp),this.state.player.hp>0&&n.a.createElement("span",{className:"level-item"},n.a.createElement("img",{src:"/images/double07/heart.png",alt:"Heart"})," "),this.state.player.hp>1&&n.a.createElement("span",{className:"level-item"},n.a.createElement("img",{src:"/images/double07/heart.png",alt:"Heart"})," "),this.state.player.hp>2&&n.a.createElement("span",{className:"level-item"},n.a.createElement("img",{src:"/images/double07/heart.png",alt:"Heart"}))),n.a.createElement("div",{className:"level-item"},n.a.createElement("button",{className:"button is-white"},"Action Points: ",this.state.player.ap)))),n.a.createElement("div",{className:"box"},n.a.createElement("div",{className:"buttons"},n.a.createElement("button",{className:"attack"===this.state.action?"button is-fullwidth is-danger":"button is-fullwidth is-dark",onClick:function(){return e.chooseAction("attack")},disabled:0===this.state.player.ap||"dead"===this.state.player.hp},"Attack"),n.a.createElement("button",{className:"defend"===this.state.action?"button is-fullwidth is-danger":"button is-fullwidth is-dark",onClick:function(){return e.chooseAction("defend")},disabled:0===this.state.player.ap||"dead"===this.state.player.hp},"Defend"),n.a.createElement("button",{className:"reload"===this.state.action?"button is-fullwidth is-danger":"button is-fullwidth is-dark",onClick:function(){return e.chooseAction("reload")},disabled:0===this.state.player.ap||"dead"===this.state.player.hp},"Reload"))))))),n.a.createElement("div",{className:this.state.showTargets?"modal is-active":"modal"},n.a.createElement("div",{className:"modal-background"}),n.a.createElement("div",{className:"modal-content"},n.a.createElement("div",{className:"box has-text-centered"},n.a.createElement("div",{className:"columns is-centered"},n.a.createElement("div",{className:"column is-7"},n.a.createElement("h5",{className:"title is-5"},"Choose a Target"),this.state.allTargets.map(function(t,a){return n.a.createElement("div",{className:e.state.target.username===t.username?"button level is-mobile is-danger":"button level is-mobile is-dark",key:a,onClick:function(){return e.choosePlayer(t.username)}},n.a.createElement("div",{className:"level-left"},n.a.createElement("div",{className:"level-item"},n.a.createElement("span",null,t.username)),n.a.createElement("div",{className:"level-item"},n.a.createElement("span",null,"HP: ",t.hp," "))),n.a.createElement("div",{className:"level-right"},t.hp>0&&n.a.createElement("span",{className:"level-item"},n.a.createElement("img",{src:"/images/double07/heart.png",alt:"Heart"})),t.hp>1&&n.a.createElement("span",{className:"level-item"},n.a.createElement("img",{src:"/images/double07/heart.png",alt:"Heart"})),t.hp>2&&n.a.createElement("span",{className:"level-item"},n.a.createElement("img",{src:"/images/double07/heart.png",alt:"Heart"}))))}))))),n.a.createElement("button",{className:"modal-close is-large","aria-label":"close",onClick:this.closeTargetList})))}}]),t}(n.a.Component),k=a(37),S=a.n(k),y=function(e){function t(e){var a;return Object(c.a)(this,t),(a=Object(o.a)(this,Object(m.a)(t).call(this,e))).updateTimer=function(){a.setState({timer:a.state.timer+1})},a.endOfTurn=function(){!0===a.state.userTurn&&(a.props.socket.emit("endOfTurn",{player:a.state.potatoHolder,time:a.state.timer}),a.setState({userTurn:!1,handImage:"/images/hand.png"}),clearInterval(a.interval))},a.state={timer:0,potatoHolder:"",userTurn:!1,explode:!1,handImage:"/images/hand.png"},a}return Object(u.a)(t,e),Object(l.a)(t,[{key:"componentDidMount",value:function(){var e=this,t=document.getElementById("swipePotato");new S.a(t).on("swipe",this.endOfTurn),this.props.socket.on("state",function(t){e.props.userState.username===t.next&&e.setState({userTurn:!0,timer:0,explode:!1,handImage:"/images/hand_with_potato.png"},function(){e.interval=setInterval(function(){return e.updateTimer()},1e3)}),e.setState({potatoHolder:t.next})}),this.props.socket.on("explode",function(){clearInterval(e.interval),e.setState({userTurn:!1,explode:!0}),e.props.socket.emit("endOfTurn",{player:e.state.potatoHolder})}),window.addEventListener("beforeunload",function(e){e.returnValue="Refreshing the page will break things"})}},{key:"componentWillUnmount",value:function(){this.props.socket.removeAllListeners()}},{key:"render",value:function(){return n.a.createElement("div",{className:"hero is-fullheight"},n.a.createElement("div",{className:"hero-body"},n.a.createElement("div",{className:"container has-text-centered"},n.a.createElement("div",{className:"columns is-centered"},n.a.createElement("div",{className:"column is-5"},n.a.createElement("h1",{className:"landing title is-1 has-text-white"},"Hot Potato"),n.a.createElement("div",{className:this.state.userTurn?"box":"box is-hidden"},n.a.createElement("h3",{className:"title is-3"},"Time Held"),n.a.createElement("h5",{className:"title is-5"},this.state.timer," Seconds")),n.a.createElement("div",{className:this.state.userTurn?"box is-hidden":"box"},n.a.createElement("h3",{className:"title is-3"},"Player with Potato"),n.a.createElement("h5",{className:"title is-5"},this.state.potatoHolder)),n.a.createElement("div",{className:"box"},n.a.createElement("img",{id:"swipePotato",src:!0===this.state.explode?"/images/hand_with_explosion.png":this.state.handImage,alt:"Pass Potato"}),n.a.createElement("h6",{className:!0===this.state.userTurn?"title is-6":"is-hidden"},"Swipe Left or Right To Pass The Potato")))))))}}]),t}(n.a.Component),w=function(e){function t(e){var a;return Object(c.a)(this,t),(a=Object(o.a)(this,Object(m.a)(t).call(this,e))).findUnselectable=function(e){var t;for(t=0;t<a.state.unselectableCards.length;t++)a.state.unselectableCards[t][0]===e[0]&&a.state.unselectableCards[t][1]===e[1]&&a.setState({disableSubmit:!0,cursor:e})},a.submitDirection=function(e){a.setState({disableSubmit:!1},function(){a.props.socket.emit(e)})},a.selectCard=function(){a.setState({cardValue:a.state.board[a.state.cursor[0]][a.state.cursor[1]],cardSelected:!0}),a.props.socket.emit("select")},a.flipCard=function(){a.setState({flip:!1},function(){clearInterval(a.interval),a.interval=setInterval(function(){return a.hideBox()},1e3)})},a.hideBox=function(){clearInterval(a.interval),a.setState({cardSelected:!1})},a.state={flip:!1,playersTurn:!1,cursor:[],board:[],unselectableCards:[],cardSelected:!1,cardValue:"",disableSubmit:!1},a}return Object(u.a)(t,e),Object(l.a)(t,[{key:"componentDidMount",value:function(){var e=this;this.props.socket.on("turn",function(t){var a,s;t.next[0]===e.props.userState.username?e.setState({playersTurn:!0,cursor:t.cursor,board:t.board}):e.setState({playersTurn:!1});var n=[];for(a=0;a<t.gameBoard.length;a++)for(s=0;s<t.gameBoard[0].length;s++)"XX"!==t.gameBoard[a][s]&&n.push([a,s]);e.setState({unselectableCards:n},function(){console.log(e.state.unselectableCards),e.findUnselectable(t.cursor)}),console.log(t)}),this.props.socket.on("flip",function(t){console.log("flip"),e.interval=setInterval(function(){return e.flipCard()},5e3),e.setState({flip:!0,playersTurn:!1})}),this.props.socket.on("cursor",function(t){e.findUnselectable(t),e.setState({cursor:t}),console.log(t)}),this.props.socket.on("timeout",function(e){console.log("timeout")}),window.addEventListener("beforeunload",function(e){e.returnValue="Refreshing the page will break things"})}},{key:"componentWillUnmount",value:function(){this.props.socket.removeAllListeners()}},{key:"render",value:function(){var e=this;return n.a.createElement("div",{className:"hero is-fullheight"},n.a.createElement("div",{className:"hero-body"},n.a.createElement("div",{className:"container has-text-centered"},n.a.createElement("div",{className:"columns is-centered"},n.a.createElement("div",{className:"column is-4"},n.a.createElement("div",{className:!0===this.state.cardSelected?"box":"box is-hidden"},n.a.createElement("div",{className:!0===this.state.flip?"flip-container flip":"flip-container"},n.a.createElement("div",{className:"flipper"},n.a.createElement("div",{className:"front"},n.a.createElement("img",{src:"/images/match/cards/card_back.png",alt:"Card Back"})),n.a.createElement("div",{className:"back"},n.a.createElement("img",{src:"/images/match/cards/card_".concat(this.state.cardValue,".png"),alt:"Card ".concat(this.state.cardValue)}))))),n.a.createElement("div",{className:!1===this.state.cardSelected?"box":"box is-hidden"},n.a.createElement("h2",{className:"title is-2"},"Select A Card")),n.a.createElement("div",{className:"box"},n.a.createElement("div",{className:"field is-grouped is-grouped-centered"},n.a.createElement("div",{className:"control"},n.a.createElement("button",{className:"button is-large noButton",disabled:!0})),n.a.createElement("div",{className:"control"},n.a.createElement("button",{className:"button is-info is-large",disabled:!1===this.state.playersTurn,onClick:function(){return e.submitDirection("up")}},n.a.createElement("img",{src:"/images/match/up_chevron.png",alt:"UP"}))),n.a.createElement("div",{className:"control"},n.a.createElement("button",{className:"button is-large noButton",disabled:!0}))),n.a.createElement("div",{className:"field is-grouped is-grouped-centered"},n.a.createElement("div",{className:"control"},n.a.createElement("button",{className:"button is-info is-large",disabled:!1===this.state.playersTurn,onClick:function(){return e.submitDirection("left")}},n.a.createElement("img",{src:"/images/match/left_chevron.png",alt:"LEFT"}))),n.a.createElement("div",{className:"control"},n.a.createElement("button",{className:"button is-info is-large",disabled:!1===this.state.playersTurn||!0===this.state.disableSubmit,onClick:this.selectCard},n.a.createElement("img",{src:"/images/match/dot_and_circle.png",alt:"SUBMIT"}))),n.a.createElement("div",{className:"control"},n.a.createElement("button",{className:"button is-info is-large",disabled:!1===this.state.playersTurn,onClick:function(){return e.submitDirection("right")}},n.a.createElement("img",{src:"/images/match/right_chevron.png",alt:"RIGHT"})))),n.a.createElement("div",{className:"field is-grouped is-grouped-centered"},n.a.createElement("div",{className:"control"},n.a.createElement("button",{className:"button is-large noButton",disabled:!0})),n.a.createElement("div",{className:"control"},n.a.createElement("button",{className:"button is-info is-large",disabled:!1===this.state.playersTurn,onClick:function(){return e.submitDirection("down")}},n.a.createElement("img",{src:"/images/match/down_chevron.png",alt:"DOWN"}))),n.a.createElement("div",{className:"control"},n.a.createElement("button",{className:"button is-large noButton",disabled:!0})))))))))}}]),t}(n.a.Component),O=function(e){function t(e){var a;return Object(c.a)(this,t),(a=Object(o.a)(this,Object(m.a)(t).call(this,e))).selectPicture=function(e){a.state.fragmentChosen||(console.log(e),a.setState({fragmentChosen:!0},function(){a.props.socket.emit("select",{player:a.props.userState.username,selection:e})}))},a.state={fragments:[],fragmentChosen:!1},a}return Object(u.a)(t,e),Object(l.a)(t,[{key:"componentDidMount",value:function(){var e=this;this.props.socket.on("turn",function(t){console.log(t),e.setState({fragments:t.fragments,fragmentChosen:!1})}),window.addEventListener("beforeunload",function(e){e.returnValue="Refreshing the page will break things"})}},{key:"render",value:function(){var e=this;return n.a.createElement("div",{className:"hero is-fullheight"},n.a.createElement("div",{className:"hero-body"},n.a.createElement("div",{className:"container has-text-centered"},n.a.createElement("div",{className:"columns is-1 is-variable is-mobile is-centered"},n.a.createElement("div",{className:"column is-one-fifth-desktop"},n.a.createElement("div",{className:"level"},n.a.createElement("img",{className:"image level-item",src:"../images/fragments/".concat(this.state.fragments[0]),alt:"Fragment 1",onClick:function(){return e.selectPicture(e.state.fragments[0])}})),n.a.createElement("div",{className:"level"},n.a.createElement("img",{className:"image level-item",src:"../images/fragments/".concat(this.state.fragments[3]),alt:"Fragment 4",onClick:function(){return e.selectPicture(e.state.fragments[3])}})),n.a.createElement("div",{className:"level"},n.a.createElement("img",{className:"image level-item",src:"../images/fragments/".concat(this.state.fragments[6]),alt:"Fragment 7",onClick:function(){return e.selectPicture(e.state.fragments[6])}}))),n.a.createElement("div",{className:"column is-one-fifth-desktop"},n.a.createElement("div",{className:"level"},n.a.createElement("img",{className:"image level-item",src:"../images/fragments/".concat(this.state.fragments[1]),alt:"Fragment 2",onClick:function(){return e.selectPicture(e.state.fragments[1])}})),n.a.createElement("div",{className:"level"},n.a.createElement("img",{className:"image level-item",src:"../images/fragments/".concat(this.state.fragments[4]),alt:"Fragment 5",onClick:function(){return e.selectPicture(e.state.fragments[4])}})),n.a.createElement("div",{className:"level"},n.a.createElement("img",{className:"image level-item",src:"../images/fragments/".concat(this.state.fragments[7]),alt:"Fragment 8",onClick:function(){return e.selectPicture(e.state.fragments[7])}}))),n.a.createElement("div",{className:"column is-one-fifth-desktop"},n.a.createElement("div",{className:"level"},n.a.createElement("img",{className:"image level-item",src:"../images/fragments/".concat(this.state.fragments[2]),alt:"Fragment 3",onClick:function(){return e.selectPicture(e.state.fragments[2])}})),n.a.createElement("div",{className:"level"},n.a.createElement("img",{className:"image level-item",src:"../images/fragments/".concat(this.state.fragments[5]),alt:"Fragment 6",onClick:function(){return e.selectPicture(e.state.fragments[5])}})),n.a.createElement("div",{className:"level"},n.a.createElement("img",{className:"image level-item",src:"../images/fragments/".concat(this.state.fragments[8]),alt:"Fragment 9",onClick:function(){return e.selectPicture(e.state.fragments[8])}}))))),n.a.createElement("div",{className:this.state.fragmentChosen?"modal is-active":"modal"},n.a.createElement("div",{className:"modal-background"}),n.a.createElement("div",{className:"modal-content"},n.a.createElement("div",{className:"box has-text-centered"},n.a.createElement("h5",{className:"title is-5"},"Fragment Chosen"))))))}}]),t}(n.a.Component),C=function(e){function t(e){var a;return Object(c.a)(this,t),(a=Object(o.a)(this,Object(m.a)(t).call(this,e))).submitTap=function(){a.setState({tapCount:a.state.tapCount+1})},a.submitSimon=function(e){var t=[];(t=a.state.simonSequence).push(e),a.setState({simonSequence:t})},a.submitMaff=function(e){"delete"===e?a.setState({mathAnswer:Math.trunc(a.state.mathAnswer/10)}):"minus"===e?a.setState({mathAnswer:-1*a.state.mathAnswer}):a.setState({mathAnswer:10*a.state.mathAnswer+e})},a.state={name:"",valid:"",playerHealth:"",tapCount:0,simonSequence:[],mathAnswer:0,activateButton:0},a}return Object(u.a)(t,e),Object(l.a)(t,[{key:"componentDidMount",value:function(){var e=this;this.props.socket.on("state",function(t){var a=e.props.userState.username;e.setState({name:t.name,valid:t.valid,playerHealth:t.players[a].hp,tapCount:0,simonSequence:[],mathAnswer:0}),console.log(t),console.log("Player Health: "+e.state.playerHealth)}),this.props.socket.on("timerExpired",function(t){var a;console.log("timerExpired"),"MultiTap"===e.state.name?a=e.state.tapCount:"QuickMaff"===e.state.name?(a=e.state.mathAnswer,console.log(a)):a=e.state.simonSequence,e.props.socket.emit("action",{player:e.props.userState.username,valid:a})}),window.addEventListener("beforeunload",function(e){e.returnValue="Refreshing the page will break things"})}},{key:"componentWillUnmount",value:function(){this.props.socket.removeAllListeners()}},{key:"render",value:function(){var e=this;return n.a.createElement("div",{className:"hero is-fullheight"},n.a.createElement("div",{className:"hero-body"},n.a.createElement("div",{className:"container has-text-centered"},n.a.createElement("div",{className:"columns is-centered"},n.a.createElement("div",{className:"column is-5"},n.a.createElement("div",{className:"Simon"===this.state.name?"box":"box is-hidden"},n.a.createElement("div",{className:"columns is-1 is-variable is-mobile"},n.a.createElement("div",{className:"column"},n.a.createElement("div",{className:"buttons"},n.a.createElement("span",{className:"button is-fullwidth is-large is-success",onClick:function(){return e.submitSimon("Green")}},"G"),n.a.createElement("span",{className:"button is-fullwidth is-large is-danger",onClick:function(){return e.submitSimon("Red")}},"R"))),n.a.createElement("div",{className:"column"},n.a.createElement("div",{className:"buttons"},n.a.createElement("span",{className:"button is-fullwidth is-large is-warning",onClick:function(){return e.submitSimon("Yellow")}},"Y"),n.a.createElement("span",{className:"button is-fullwidth is-large is-info",onClick:function(){return e.submitSimon("Blue")}},"B"))))),n.a.createElement("div",{className:"MultiTap"===this.state.name?"box multiTap":"box is-hidden",onClick:this.submitTap},n.a.createElement("h5",{className:"title is-5"},"Tap Here")),n.a.createElement("div",{className:"QuickMaff"===this.state.name?"box":"box is-hidden"},n.a.createElement("h4",{className:"title is-4"},"QuickMaff"),n.a.createElement("div",{className:"field"},n.a.createElement("div",{className:"control"},n.a.createElement("input",{className:"input is-medium",type:"text",value:this.state.mathAnswer,readOnly:!0}))),n.a.createElement("div",{className:"columns is-1 is-variable is-mobile"},n.a.createElement("div",{className:"column"},n.a.createElement("div",{className:"buttons"},n.a.createElement("span",{className:"button is-fullwidth is-large is-info",onClick:function(){return e.submitMaff(1)}},"1"),n.a.createElement("span",{className:"button is-fullwidth is-large is-info",onClick:function(){return e.submitMaff(4)}},"4"),n.a.createElement("span",{className:"button is-fullwidth is-large is-info",onClick:function(){return e.submitMaff(7)}},"7"),n.a.createElement("span",{className:"button is-fullwidth is-large is-info",onClick:function(){return e.submitMaff("minus")}},"-"))),n.a.createElement("div",{className:"column"},n.a.createElement("div",{className:"buttons"},n.a.createElement("span",{className:"button is-fullwidth is-large is-info",onClick:function(){return e.submitMaff(2)}},"2"),n.a.createElement("span",{className:"button is-fullwidth is-large is-info",onClick:function(){return e.submitMaff(5)}},"5"),n.a.createElement("span",{className:"button is-fullwidth is-large is-info",onClick:function(){return e.submitMaff(8)}},"8"),n.a.createElement("span",{className:"button is-fullwidth is-large is-info",onClick:function(){return e.submitMaff(0)}},"0"))),n.a.createElement("div",{className:"column"},n.a.createElement("div",{className:"buttons"},n.a.createElement("span",{className:"button is-fullwidth is-large is-info",onClick:function(){return e.submitMaff(3)}},"3"),n.a.createElement("span",{className:"button is-fullwidth is-large is-info",onClick:function(){return e.submitMaff(6)}},"6"),n.a.createElement("span",{className:"button is-fullwidth is-large is-info",onClick:function(){return e.submitMaff(9)}},"9"),n.a.createElement("span",{className:"button is-fullwidth is-large is-info",onClick:function(){return e.submitMaff("delete")}},n.a.createElement("img",{src:"/images/multigame/reply.png",alt:"Delete"}))))))))),n.a.createElement("div",{className:"dead"===this.state.playerHealth?"modal is-active":"modal"},n.a.createElement("div",{className:"modal-background"}),n.a.createElement("div",{className:"modal-content"},n.a.createElement("div",{className:"box has-text-centered"},n.a.createElement("h5",{className:"title is-5"},"You Are Dead"))))))}}]),t}(n.a.Component),j=function(e){function t(){return Object(c.a)(this,t),Object(o.a)(this,Object(m.a)(t).apply(this,arguments))}return Object(u.a)(t,e),Object(l.a)(t,[{key:"render",value:function(){return n.a.createElement("h1",null,"Page Not Found")}}]),t}(n.a.Component),T=a(38),x=a.n(T),I=function(e){function t(e){var a;return Object(c.a)(this,t),(a=Object(o.a)(this,Object(m.a)(t).call(this,e))).updateUsername=function(e){a.setState({username:e}),sessionStorage.setItem("username",e)},a.updateSocketId=function(e){a.setState({socketId:e}),sessionStorage.setItem("socketId",e)},a.updateGameList=function(e){a.setState({gameList:e}),sessionStorage.setItem("gameList",e)},a.state={username:"",socket:"",gameList:[]},a.socket=x()(),a}return Object(u.a)(t,e),Object(l.a)(t,[{key:"render",value:function(){var e=this;return n.a.createElement(d.a,null,n.a.createElement(h.a,null,n.a.createElement(p.a,{exact:!0,path:"/",render:function(t){return n.a.createElement(f,Object.assign({},t,{userState:e.state,socket:e.socket,updateUsername:e.updateUsername,updateSocketId:e.updateSocketId,updateGameList:e.updateGameList}))}}),n.a.createElement(p.a,{path:"/room",render:function(t){return n.a.createElement(E,Object.assign({},t,{userState:e.state,socket:e.socket}))}}),n.a.createElement(p.a,{path:"/Double07",render:function(t){return n.a.createElement(N,Object.assign({},t,{userState:e.state,socket:e.socket}))}}),n.a.createElement(p.a,{path:"/Hot_Potato",render:function(t){return n.a.createElement(y,Object.assign({},t,{userState:e.state,socket:e.socket}))}}),n.a.createElement(p.a,{path:"/Match",render:function(t){return n.a.createElement(w,Object.assign({},t,{userState:e.state,socket:e.socket}))}}),n.a.createElement(p.a,{path:"/Fragments",render:function(t){return n.a.createElement(O,Object.assign({},t,{userState:e.state,socket:e.socket}))}}),n.a.createElement(p.a,{path:"/MultiGame",render:function(t){return n.a.createElement(C,Object.assign({},t,{userState:e.state,socket:e.socket}))}}),n.a.createElement(p.a,{path:"/",component:j})))}}]),t}(s.Component);a(76),a(78);i.a.render(n.a.createElement(I,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then(function(e){e.unregister()})}},[[40,2,1]]]);
//# sourceMappingURL=main.5543472e.chunk.js.map