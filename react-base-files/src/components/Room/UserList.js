import React from 'react';

class UserList extends React.Component {
    render() {
        return (
            <div className="box">
                <h1 className="title">Users</h1>
                <div className="content">
                    <div className="buttons">
                        {this.props.users.map((user, index) => (
                            <span className="button" key={index}>{user.username}</span>
                        ))} 
                    </div>                                      
                </div>             
            </div>
        );
    }
}

export default UserList;