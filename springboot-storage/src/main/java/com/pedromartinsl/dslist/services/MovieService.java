package com.pedromartinsl.dslist.services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.bind.annotation.PathVariable;

import com.pedromartinsl.dslist.dto.MovieDTO;
import com.pedromartinsl.dslist.dto.MovieMinDTO;
import com.pedromartinsl.dslist.entities.Movie;
import com.pedromartinsl.dslist.projections.MovieMinProjection;
import com.pedromartinsl.dslist.repositories.MovieRepository;


@Service
public class MovieService {
    
    @Autowired
	private MovieRepository movieRepository;

	@Transactional(readOnly = true)
	public MovieDTO findById(@PathVariable Long listId) {
		Movie result = movieRepository.findById(listId).get();
		return new MovieDTO(result);
	}
	
	public List<MovieMinDTO> findAll() {
		List<Movie> result = movieRepository.findAll();
		return result.stream().map(MovieMinDTO::new).toList();
	}

	@Transactional(readOnly = true)
	public List<MovieMinDTO> findByMovieList(Long listId) {
		List<MovieMinProjection> movies = movieRepository.searchByList(listId);
		return movies.stream().map(MovieMinDTO::new).toList();
	}
	
}
