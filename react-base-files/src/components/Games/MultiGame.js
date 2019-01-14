import React from 'react';

class MultiGame extends React.Component {
    componentDidMount() {
        this.props.socket.on('state', (data) => {
            console.log(data);
        });
    }
    
    render() {
        return (
            <div className="hero is-fullheight">
                <div className="hero-body">
                    <div className="container has-text-centered">
                        <div className="column is-5">
                            <div className="box"></div>
                            <div className="box"></div>
                            <div className="box"></div>
                        </div>
                    </div>
                </div>  
            </div>
        );
    }
}

export default MultiGame;