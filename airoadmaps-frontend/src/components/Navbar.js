
'use client'

import { useUser } from '@/context/UserContext';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { useRef } from 'react';

const Navbar = () => {
    const path = usePathname();
    const menu = useRef();
    const { user, logout } = useUser();

    const toggleMenu = () => {
        menu.current.classList.toggle("active")

    }




    return (
        <nav className='navbar'>
            <Link  href={"/"} className='logo-container text-lg font-medium'>AI Roadmaps</Link>
            <div className='toggle-button-container'>
                <button onClick={toggleMenu} className="toggle-button">
                    <span className="bar"></span>
                    <span className="bar"></span>
                    <span className="bar"></span>

                </button>
            </div>
            <div ref={menu} className="nav-menu-wrapper">
                <ul className="nav-menu">
                    <li><Link onClick={toggleMenu} className={path === '/create' ? 'active' : ''} href="/create"> Create</Link></li>
                    <li><Link onClick={toggleMenu} className={path === '/list-roadmaps' ? 'active' : ''} href="/list-roadmaps"> Your Roadmaps</Link></li>
                </ul>
                <div>
                    {user.loggedIn ? <button onClick={() => {
                        logout();
                        window.location.href = "/"
                    }
                    } className='bg-accent p-1.5 rounded p-1.5'>Logout</button> :
                        <Link  onClick={toggleMenu}  href={"/auth"} className='bg-accent p-1.5 rounded p-1.5'>Login</Link>
                    }
                </div>
            </div>

        </nav>
    );
};

export default Navbar;
