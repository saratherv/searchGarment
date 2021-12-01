import React, { useState } from 'react';
import Scroll from './Scroll';
import SearchList from './SearchList';

function Search() {

  const [searchShow, setSearchShow] = useState(false);
  const [data, setData] = useState("")

  const handleChange = e => {
    // setSearchField(e.target.value);
    if(e.target.value===""){
      setSearchShow(false);
    }
    else {
    fetch("http://0.0.0.0:8080/search/" + e.target.value, {method: 'GET'})
    .then(response => response.json())
    .then(result => {
      if(result.success===true){
        setData(result.data)
        setSearchShow(true);
      }
    })
    .catch(error => console.log('error', error));
    }
  };

  function searchList() {
  	if (searchShow && data !== "") {
	  	return (
	  		<Scroll>
	  			<SearchList filteredGarments={data} />
	  		</Scroll>
	  	);
	  }
  }

  return (
    <section className="garamond">
			<div className="navy georgia ma0 grow">
				<h2 className="f2">Garment Store</h2>
			</div>
			<div className="pa2">
				<input 
					className="pa3 bb br3 grow b--none bg-lightest-blue ma3"
					type = "search" 
					placeholder = "Search Items" 
					onChange = {handleChange}
				/>
			</div>
			{searchList()}
		</section>
  );
}

export default Search;