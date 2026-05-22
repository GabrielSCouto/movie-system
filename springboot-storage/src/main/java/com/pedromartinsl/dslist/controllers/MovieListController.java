package com.pedromartinsl.dslist.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.pedromartinsl.dslist.dto.MovieListDTO;
import com.pedromartinsl.dslist.dto.MovieMinDTO;
import com.pedromartinsl.dslist.dto.ReplacementDTO;
import com.pedromartinsl.dslist.services.MovieService;
import com.pedromartinsl.dslist.services.MovieListService;

@RestController
@RequestMapping(value = "/lists")
public class MovieListController {

	@Autowired
	private MovieListService movieListService;
	
	@Autowired
	private MovieService movieService;

	@GetMapping
	public List<MovieListDTO> findAll() {
		List<MovieListDTO> result = movieListService.findAll();
		return result;
	}

	@GetMapping(value = "/{listId}/movies")
	public List<MovieMinDTO> findGames(@PathVariable Long listId) {
		List<MovieMinDTO> result = movieService.findByMovieList(listId);
		return result;
	}

	@PostMapping(value = "/{listId}/replacement")
	public void move(@PathVariable Long listId, @RequestBody ReplacementDTO body) {
		movieListService.move(listId, body.getSourceIndex(), body.getDestinationIndex());
	}
}