import React from 'react';
import Card from './Card';

function SearchList({ filteredGarments }) {
  const filtered = filteredGarments.map( garment =>  <Card key={garment.product_id} garment={garment} />); 
  return (
    <div>
      {filtered}
    </div>
  );
}

export default SearchList;