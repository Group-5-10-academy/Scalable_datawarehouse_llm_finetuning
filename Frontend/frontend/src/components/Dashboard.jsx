import React, { useContext, useEffect, useState } from "react";

import Header from "./header";
import Details from "./details";
import Overview from "./Overview";





const Dashboard = () => {
  const [stockDetails, setStockDetails] = useState({});
  
  return (
    <div
      className="h-screen bg-neutral-100 grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 grid-rows-8 md:grid-rows-7 xl:grid-rows-5 auto-rows-fr gap-6 p-10 font-quicksand 
        bg-slate-900 text-gray-500 bg-neutral-100"
    
    >
      <div className="col-span-1  md:col-span-2 xl:col-span-3 row-span-1 space-y-1 flex justify-start items-center border-white">
        <Header name={"name"} />
        
      </div>
      

      <div className="row-span-2">
        { <Overview 
         symbol={"Symbol"}
         price={"quote"}
         change={"quote"}
         changePercent={"quote"}
         currency={"currency"}/> }
          
        
      </div>
      <div className="row-span-2 xl:row-span-4">
        { <Details details={stockDetails}
                      /> }
      </div>
    </div>
  );
};

export default Dashboard;