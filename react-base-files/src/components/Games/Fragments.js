import React from 'react';

class Fragments extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            fragments: []
        }
    }

    componentDidMount() {
        this.props.socket.on('turn', (data) => {
            console.log(data);
            this.setState({ fragments: data.fragments });
        });
    }

    selectPicture = (data) => {
        this.props.socket.emit('select', data);
    }
    
    render() {
        return (
            <div className="hero is-fullheight">
                <div className="hero-body">
                    <div className="container has-text-centered">
                        <h1 className="landing title is-1 has-text-white">Fragments</h1>
                        <div className="box">
                            <figure>
                                {this.state.fragments.map((fragment, index) => (
                                    <img
                                        src={`/images/${fragment}`}
                                        alt={fragment}
                                        onClick={() => this.selectPicture(fragment)}
                                    />   
                                ))}
                                
                            </figure>
                        </div>
                    </div>
                </div>  
            </div>
        );
    }
}

export default Fragments;