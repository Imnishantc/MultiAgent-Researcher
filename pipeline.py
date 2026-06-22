from agents import  build_search_agent , build_scraping_agent , writer_chain , critic_chain

#Pipeline Function
def run_research_pipeline(topic:str) -> dict:

    state ={}

    #search agent working
    
    print("\n"+" ="*50)
    print("step 1 - search agent is working ...")
    print("="*50)

    search_agent = build_search_agent()
    search_result = search_agent.invoke({
        "messages" : [("user", f"Find recent, reliable and detailed information on the topic: {topic}")]
    })

    state["search_result"] = search_result["messages"][-1].content
    
    print("\n search result ",state['search_result'])

    #scraping agent working 

    print("\n"+" ="*50)
    print("step 2 - scraping agent is working ...")
    print("="*50)

    scraping_agent = build_scraping_agent()
    scraping_result = scraping_agent.invoke({
        "messages" : [("user",
                       f"Based on the following search results about '{topic}',"
                       f"Pick the most relevant URL and scrape detailed information from it for deeper insights.\n\n"
                       f"Search Results:\n{state['search_result'][:800]}"
                    )]
    })


    state["scraping_result"] = scraping_result["messages"][-1].content
    
    print("\nscraped result: \n", state['scraping_result'])


    #writer chain working

    print("\n"+" ="*50)
    print("step 3 - Writer is drafting the report ...")
    print("="*50)

    research_combined =(
        f"SEARCH RESULTS: \n {state['search_result']} \n\n"
        f"SCRAPING RESULTS: \n {state['scraping_result']}"
    )

    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })

    print("\nGenerated Report:\n", state["report"])


    #critic chain working

    print("\n"+" ="*50)
    print("step 4 - critic is reviewing the report ")
    print("="*50)

    state["feedback"] = critic_chain.invoke({
        "report": state["report"]
    })  

    print("\n critic report \n", state['feedback'])

    return state



if __name__ == "__main__":                          # to call pipeline.py
    topic = input("\n Enter a research topic: ")
    run_research_pipeline(topic)