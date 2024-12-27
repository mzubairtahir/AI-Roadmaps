// src/app/layout.js
import { GoogleOAuthProvider } from '@react-oauth/google';
import "./globals.css"
import Navbar from '@/components/Navbar';
import { UserProvider } from '@/context/UserContext';
import { cookies } from 'next/headers';

const clientId = process.env.GOOGLE_CLIENT_ID; // Replace with your client ID


const getData = async () => {
  const cookieStore = cookies();
  let { value: sessionId } = cookieStore.get("sessionid") || {};


  try {

    const response = await fetch("http://127.0.0.1:8000/api/auth/session", {
      headers: {
        Cookie: `sessionid=${sessionId}`
      }
    });
    if (response.ok) {
      const data = await response.json();

      return data;
    }

  }
  catch (err) {
    return;

  }
}
const RootLayout = async ({ children }) => {
  const data = await getData();
  const initialState = data ? {
    "loggedIn": true,
    "userId": data.user
  } : {
    "loggedIn": false,
    "userId": null
  }



  return (
    <GoogleOAuthProvider clientId={clientId}>
      <UserProvider initial_state={initialState}>

        <html lang="en">
          <body>
            <Navbar />
            <div>

              {children}
            </div>

          </body>
        </html>
      </UserProvider>

    </GoogleOAuthProvider>
  );
}
  ;

export default RootLayout;
