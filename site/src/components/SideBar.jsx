const SideBar = () => {
    return (
      <aside className= "bg-slate-100 space-y-2 max-w-prose p-4 h-screen border-r-4 border-slate-500 border-dashed">
        <nav>
          <ul>
          {/* <li>
              <a href="/note" className="block py-2 px-4 rounded hover:bg-slate-200 transition-all text-slate-900 hover:text-cyan-800">
                Troubleshooting
              </a>
            </li> */}
            <li>
              <a href="/guide" className="block py-2 px-4 rounded hover:bg-slate-200 transition-all text-slate-900 hover:text-cyan-800">
                DIY Guide
              </a>
            </li>
          </ul>
        </nav>
      </aside>
    );
  };
  
  export default SideBar;