import React, { useState } from 'react';
import Scroll from './Scroll';
import SearchList from './SearchList';

function Search() {

  const [searchShow, setSearchShow] = useState(false);
  const [data, setData] = useState("")
  const [offset, setOffset] = useState(0)
  const [searchValue, setSearchValue] = useState("")

  const handleChange = e => {
    // setSearchField(e.target.value);
    if(e.target.value==="" || e.target.value.length<3){
      setSearchShow(false);
    }
    else {
      setSearchValue(e.target.value)
    fetch("http://0.0.0.0:8080/search?searchValue=" + e.target.value + "&offset=" + offset, {method: 'GET'})
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

  function load_more() {
    setOffset(offset+ 50)
    fetch("http://0.0.0.0:8080/search?searchValue=" + searchValue + "&offset=" + offset, {method: 'GET'})
    .then(response => response.json())
    .then(result => {
      if(result.success===true){
        setData(result.data)
        setSearchShow(true);
      }
    })
    .catch(error => console.log('error', error));
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

      {searchShow === true ? <button onClick={ load_more }> load more </button> : null}
		</section>
  );
}

export default Search;