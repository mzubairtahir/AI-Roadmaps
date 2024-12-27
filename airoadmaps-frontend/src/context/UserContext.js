'use client';

const { createContext, useState, useContext, useEffect } = require("react");


const UserContext = createContext();

export const UserProvider = ({ children, initial_state }) => {
    const [user, setUser] = useState(initial_state);
    


    const login = (userId) => {
        setUser({
            "loggedIn": true,
            "userId": userId
        })
    }

    const logout = async () => {
        try {
            const response = await fetch("/api/auth/logout", {
                method: "post"
            });
            if (response.ok) {
                setUser({
                    "loggedIn": false,
                    "userId": null
                });
            }
        }
        catch (error) {

        }


    }


    return (
        <UserContext.Provider value={{ user, login, logout}}>
            {children}
        </UserContext.Provider>
    )



}


export const useUser = () => useContext(UserContext);

