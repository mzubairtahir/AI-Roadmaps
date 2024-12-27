
const { default: GoogleSignIn } = require("@/components/GoogleSignIn");


export default function LoginPage() {

  
  return (
    <div>
      <div className="my-5">
        <h1 className="text-center">Login to join us!</h1>
      </div>

      <div className="flex items-center justify-center py-5">

        <GoogleSignIn />
      </div>
      <div className="flex items-center justify-center">

      </div>


    </div>
  );
}
