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
        this.props.socket.emit('select', {"selection": data});
    }
    
    render() {
        return (
            <div className="hero is-fullheight">
                <div className="hero-body">
                    <div className="container has-text-centered">
                        <div className="columns is-1 is-variable is-mobile">
                            <div className="column">
                                <img
                                    className="image"
                                    src={`/images/fragments/${this.state.fragments[0]}`}
                                    alt="Fragment 1"
                                    onClick={() => this.selectPicture(this.state.fragments[0])}
                                />
                                <img
                                    className="image"
                                    src={`/images/fragments/${this.state.fragments[3]}`}
                                    alt="Fragment 4"
                                    onClick={() => this.selectPicture(this.state.fragments[3])}
                                />
                                <img
                                    className="image"
                                    src={`/images/fragments/${this.state.fragments[6]}`}
                                    alt="Fragment 7"
                                    onClick={() => this.selectPicture(this.state.fragments[6])}
                                />
                            </div>
                            <div className="column">
                                <img
                                    className="image"
                                    src={`/images/fragments/${this.state.fragments[1]}`}
                                    alt="Fragment 2"
                                    onClick={() => this.selectPicture(this.state.fragments[1])}
                                />
                                <img
                                    className="image"
                                    src={`/images/fragments/${this.state.fragments[4]}`}
                                    alt="Fragment 5"
                                    onClick={() => this.selectPicture(this.state.fragments[4])}
                                />
                                <img
                                    className="image"
                                    src={`/images/fragments/${this.state.fragments[7]}`}
                                    alt="Fragment 8"
                                    onClick={() => this.selectPicture(this.state.fragments[7])}
                                />
                            </div>
                            <div className="column">
                                <img
                                    className="image"
                                    src={`/images/fragments/${this.state.fragments[2]}`}
                                    alt="Fragment 3"
                                    onClick={() => this.selectPicture(this.state.fragments[2])}
                                />
                                <img
                                    className="image"
                                    src={`/images/fragments/${this.state.fragments[5]}`}
                                    alt="Fragment 6"
                                    onClick={() => this.selectPicture(this.state.fragments[5])}
                                />
                                <img
                                    className="image"
                                    src={`/images/fragments/${this.state.fragments[8]}`}
                                    alt="Fragment 9"
                                    onClick={() => this.selectPicture(this.state.fragments[8])}
                                />
                            </div>
                        </div>
                    </div>
                </div>  
            </div>
        );
    }
}

export default Fragments;