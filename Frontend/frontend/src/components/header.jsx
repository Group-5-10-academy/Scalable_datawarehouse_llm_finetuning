import React from "react";
import Search from "./search";

const Header = ({name}) => {
  return (
    <div className="xl:px-32 ">
      <h1 className="text-5xl border-white">names</h1>
      <Search />
      
    </div>

  );
};

export default Header;
 