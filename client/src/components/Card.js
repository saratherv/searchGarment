import React from 'react';

function Card({garment}) {
	return(
		<div className="tc bg-light-green dib br3 pa3 ma2 grow bw2 shadow-5">
			<img className="br-100 h3 w3 dib" alt={garment.product_title} src={garment.image_urls[0]} />
			<div>
				<h7>{garment.product_title}</h7>
				<p>{garment.gender} &nbsp; {garment.price} {garment.currency_code} </p>
			</div>
		</div>
	);
 }

export default Card;