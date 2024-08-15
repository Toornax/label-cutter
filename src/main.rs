use imageproc::{
	contours::{self, find_contours}, edges::canny, gradients::{horizontal_sobel, sobel_gradients}, image::{self, io::Reader as ImageReader}
};
use std::result::Result;

fn main() -> Result<(), Box<dyn std::error::Error>>{    
	let img = ImageReader::open("images/image.jpg")?.decode()?.into_luma8();
	img.save("result/image_gray.jpg").unwrap();
	let img_sobel = image::DynamicImage::ImageLuma16(sobel_gradients(&img)).into_luma8();
	img_sobel.save("result/image_sobel.jpg").unwrap();
	let contours = find_contours::<u8>(&img_sobel);
	img.save
	// let img_canny = canny(&img_sobel, 5f32, 150f32);
	// img_canny.save("result/image_canny.jpg").unwrap();

	Ok(())
}
