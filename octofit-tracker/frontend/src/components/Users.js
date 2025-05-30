import React, { useEffect, useState } from 'react';

const API_URL = 'https://miniature-guacamole-p5p64q4wjxqh757g-8000.app.github.dev/api/users/';

function Users() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch(API_URL)
      .then(res => res.json())
      .then(data => setUsers(data.results || []));
  }, []);

  return (
    <div className="container mt-4">
      <div className="card">
        <div className="card-header bg-secondary text-white">
          <h2 className="mb-0">Users</h2>
        </div>
        <div className="card-body">
          <table className="table table-striped table-hover">
            <thead className="table-dark">
              <tr>
                <th>#</th>
                <th>Name</th>
                <th>Email</th>
              </tr>
            </thead>
            <tbody>
              {users.map((user, idx) => (
                <tr key={idx}>
                  <td>{idx + 1}</td>
                  <td>{user.name}</td>
                  <td>{user.email}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default Users;
