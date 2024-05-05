from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get('http://222.253.41.208:8100/chat/')
# Select jailbreak
select_jailbreak = Select(driver.find_element(By.ID, 'jailbreak'))
select_jailbreak.select_by_value('default')

# models = ['', 'gpt-3.5-turbo', 'gpt-3.5-turbo-0613', 'gpt-3.5-turbo-16k', 
#           'gpt-3.5-turbo-16k-0613', 'gpt-3.5-long', 'gpt-4', 'gpt-4-0613', 
#           'gpt-4-32k', 'gpt-4-32k-0613', 'llama2-7b', 'llama2-13b', 'llama2-70b', 
#           'palm2', 'palm', 'google', 'google-bard', 'google-palm', 'bard', 'falcon-40b', 
#           'falcon-7b', 'llama-13b', 'command-nightly', 'gpt-neox-20b', 'santacoder', 'bloom', 
#           'flan-t5-xxl', 'code-davinci-002', 'text-ada-001', 'text-babbage-001', 'text-curie-001', 
#           'text-davinci-002', 'text-davinci-003', 'llama70b-v2-chat', 'llama13b-v2-chat', 'llama7b-v2-chat', 
#           'oasst-sft-1-pythia-12b', 'oasst-sft-4-pythia-12b-epoch-3.5', 'command-light-nightly', 'pi']

# providers = ['', 'AItianhuSpace', 'AiChatOnline', 'Bard', 'Bing', 
#              'ChatBase', 'ChatForAi', 'Chatgpt4Online', 'ChatgptAi', 
#              'ChatgptNext', 'DeepInfra', 'FakeGpt', 'GPTalk', 'GeekGpt', 
#              'GptChatly', 'GptForLove', 'GptGo', 'GptTalkRu', 'Hashnode', 
#              'HuggingChat', 'Koala', 'Liaobots', 'Llama2', 'MyShell', 'OnlineGpt',
#                'OpenaiChat', 'PerplexityAi', 'Phind', 'Pi', 'Poe', 'Raycast', 'TalkAi', 
#                'Theb', 'ThebApi', 'You', 'Yqcloud']

models =['gpt-4', 'gpt-4-0613', 'gpt-4-32k', 'gpt-4-32k-0613']

providers = ['', 'AItianhuSpace', 'AiChatOnline', 'Bing', 
             'ChatBase', 'ChatForAi', 'Chatgpt4Online', 'ChatgptAi', 
             'ChatgptNext', 'DeepInfra', 'FakeGpt', 'GPTalk', 'GeekGpt', 
             'GptChatly', 'GptForLove', 'GptGo', 'GptTalkRu', 'Hashnode', 
             'HuggingChat', 'Koala', 'Liaobots', 'Llama2', 'MyShell', 'OnlineGpt',
               'OpenaiChat', 'PerplexityAi', 'Phind', 'Pi', 'Poe', 'Raycast', 'TalkAi', 
               'Theb', 'ThebApi', 'You', 'Yqcloud']

input_test = 'What is ChatGPT?'
c = 0
# Initialize empty lists to store data
data = {
    'Input Text': [],
    'Model': [],
    'Provider': [],
    'Response': [],
    'Response Time': [],
    'Result': []
}
for model in models:
    name_model = model
    if model == '':
        name_model = 'Model: Default'
    try:
        select_model = Select(driver.find_element(By.ID, 'model'))
        select_model.select_by_value(model)
    except:
        continue
    try:
        for provider in providers:
            try:
                c += 1
                if c % 5 == 0:
                    driver.refresh()
                    try:
                        select_model = Select(driver.find_element(By.ID, 'model'))
                        select_model.select_by_value(model)
                    except:
                        continue
                name_provider = provider
                if provider == '':
                    name_provider = 'Provider: Auto'
                try:
                    select_provider = Select(driver.find_element(By.ID, 'provider'))
                    select_provider.select_by_value(provider)
                except:
                    continue
                time.sleep(1)
                print(f"{c} - Model: {name_model}, Provider: {name_provider}")

                try:
                    input_box = driver.find_element(By.ID, 'message-input')
                    input_box.clear()
                    input_box.send_keys(input_test)

                    # Click on the element with the specified XPath
                    send_button = driver.find_element("xpath",'//*[@id="send-button"]')
                    send_button.click()

                    # Find the messages element using the provided XPath
                    messages_element = driver.find_element("xpath",'//*[@id="messages"]')
                    # Find all div elements within the messages element with class 'content' that have an ID starting with 'gpt_'
                    temp = len(messages_element.find_elements("xpath", './/div[@class="content" and starts-with(@id, "gpt_")]'))
                except:
                    driver.refresh()
                    input_box = driver.find_element(By.ID, 'message-input')
                    input_box.clear()
                    input_box.send_keys(input_test)

                    # Click on the element with the specified XPath
                    send_button = driver.find_element("xpath",'//*[@id="send-button"]')
                    send_button.click()

                    # Find the messages element using the provided XPath
                    messages_element = driver.find_element("xpath",'//*[@id="messages"]')
                    # Find all div elements within the messages element with class 'content' that have an ID starting with 'gpt_'
                    temp = len(messages_element.find_elements("xpath", './/div[@class="content" and starts-with(@id, "gpt_")]'))
                start_time = time.time()

                # Wait for generate new GPT-id messages
                while True:
                    gpt_elements = messages_element.find_elements("xpath", './/div[@class="content" and starts-with(@id, "gpt_")]')
                    if len(gpt_elements) > temp:
                        break

                # Wait for response 

                while True:

                    stop_generating_element = driver.find_element(By.CLASS_NAME, 'stop_generating')
                    sign = stop_generating_element.get_attribute('class')
                    if 'stop_generating-hidden' in sign:
                        break
                end_time = time.time()

                # Calculate the time taken
                elapsed_time = end_time - start_time
                time.sleep(2)
                gpt_ids = [element.get_attribute('id') for element in gpt_elements]
                gpt_element = driver.find_element(By.ID, gpt_ids[-1]) # get the final response
                # Extract the text associated with the GPT ID
                gpt_text = gpt_element.text

                # Append data to the lists
                data['Input Text'].append(input_test)
                data['Model'].append(name_model)
                data['Provider'].append(name_provider)
                data['Response'].append(gpt_text)
                data['Response Time'].append(elapsed_time)
                if gpt_text == '<!doctype html> <html lang=en> <title>500 Internal Server Error</title> <h1>Internal Server Error</h1> <p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>':
                    data['Result'].append(False)
                else:
                    data['Result'].append(True)
            except:
                continue
    except:
        continue
# Create a DataFrame
df = pd.DataFrame(data)

# Export the DataFrame to an Excel file
df.to_excel('D:\\autobot\\output_data4.xlsx', index=False)

# Close the webdriver
driver.quit()