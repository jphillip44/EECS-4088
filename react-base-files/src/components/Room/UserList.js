import React from 'react';

class UserList extends React.Component {
    render() {
        return (
            <div className="box">
                <h1 className="title">Users</h1>
                <div className="content">
                    {this.props.users.map((item) => (
                        <p key={item}>{item}</p>
                    ))}                    
                </div>             
            </div>
        );
    }
}

export default UserList;