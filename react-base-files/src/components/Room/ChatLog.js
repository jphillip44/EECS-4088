import React from 'react';

class ChatLog extends React.Component {
    constructor(props) {
        super(props);
        this.chatInput = React.createRef();
    }

    sendMessage = (event) => {
        event.preventDefault();
        console.log('ChatLog: ' + this.chatInput.current.value);
        this.props.sendMessage(this.chatInput.current.value);
        // Clear the username input field
        this.chatInput.current.value = '';
    }

    render() {
        let userChat = (
            <ul className="userChatLog">
                {this.props.chatLog.map((item, index) => (
                    <li key={index}>{`${item.username}: ${item.message}`}</li>
                ))}    
            </ul> 
        );

        return (
            <div className="box">
                <h1 className="title">Chat</h1>
                <div className="content">
                    {userChat}
                </div>
                <form onSubmit={this.sendMessage}>
                    <div className="field is-grouped">
                        <p className="control is-expanded">
                            <input
                                className="input"
                                type="text"
                                name="chatInput"
                                placeholder="Type text here"
                                required
                                ref={this.chatInput}
                            />
                        </p>
                        <p className="control">
                            <button className="button is-info is-fullwidth">Submit</button>
                        </p>  
                    </div>                       
                </form>
            </div>
        );
    }
}

export default ChatLog;