'use client';

import { GoogleLogin } from '@react-oauth/google';
import API from '@/utils/API';
import { useUser } from '@/context/UserContext';
import { useSearchParams } from 'next/navigation';

const GoogleSignIn = () => {
  const { user, login } = useUser();
  const params = useSearchParams();


  const loginBackend = async (access_token) => {
    try {

      const response = await API.login(access_token);
      if (response.ok) {
        const data = await response.json();
        login(data.user)
        window.location.href = params.get("next") || "/";

      }
      else {
        alert("Could not login")
      }
    }
    catch (error) {
      console.log(error);

    }

  }

  const handleLogin = (response) => {
    loginBackend(response.credential);
  };

  const handleError = (error) => {
    console.error('Login Failed: ', error);
  };

  return (
    <>
      <div>

        <div>

          <GoogleLogin
            onSuccess={handleLogin}
            onError={handleError}
          />
        </div>

      </div>
    </>
  );
};

export default GoogleSignIn;
