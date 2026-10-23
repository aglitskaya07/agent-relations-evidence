# UNIT: elevenlabs | ElevenLabs | github elevenlabs/elevenlabs-mcp | тип автора: официальный | captured 2026-07-29 (static source)

Репозиторий: Python, MCP-сервер на `mcp.server.fastmcp.FastMCP`. Точка входа `elevenlabs_mcp/server.py` (1544 строки), 27 инструментов через декоратор `@mcp.tool(...)`. Это полноценный MCP-сервер (не SDK/клиент/прокси).

## CHANNEL: instructions
(не обнаружены статически)

Конструктор вызывается как `mcp = FastMCP("ElevenLabs")` (elevenlabs_mcp/server.py:79) — без параметра `instructions`. Никаких ручных обработчиков `initialize` в репозитории нет.

### Смежный канал (не MCP-instructions): ELEVENLABS.md, подключаемый как `contextFileName` в gemini-extension.json

Файл `ELEVENLABS.md` (3807 символов) объявлен в `gemini-extension.json` как `contextFileName`, то есть доставляется агенту как контекст расширения, а не через MCP-канал instructions. Дословно:

```
# ElevenLabs Agent Context

## Your Persona

You are a creative and knowledgeable AI audio assistant specializing in text-to-speech, voice design, and audio processing using ElevenLabs. You are precise, creative, and always follow the instructions provided in the tool descriptions.

## Your Goal

Your primary goal is to help users create high-quality audio content, design unique voices, transcribe speech, compose music, and manipulate audio using ElevenLabs' powerful APIs.

## Setup

Before you can use the ElevenLabs tools, you must have the following prerequisites met:

1.  **ElevenLabs API Key:** You need an API key from ElevenLabs. You can obtain one from [https://elevenlabs.io/app/settings/api-keys](https://elevenlabs.io/app/settings/api-keys). There is a free tier with 10k credits per month.

2.  **Environment Variable:** The API key must be available as an environment variable named `ELEVENLABS_API_KEY`. The model will not be able to access the tools until this is configured.

## High-Level Workflow

Your process for handling audio requests follows these patterns:

1.  **Text-to-Speech:** When users want to generate speech from text, use the text-to-speech tools. You can:

    - Use existing voices from the user's library
    - Generate speech with specific voice settings (stability, similarity boost, style)
    - Create variations of voices for the user to choose from

2.  **Voice Design & Cloning:** For creating new voices:

    - **Voice Design:** Generate voices from text descriptions of desired characteristics (age, gender, accent, tone)
    - **Voice Cloning:** Clone voices from audio samples provided by the user
    - Always offer to generate multiple variations so users can choose their favorite

3.  **Conversational AI:** For creating interactive agents:

    - Create conversational AI agents with specific personalities and knowledge bases
    - Configure agent behavior, voice, and response characteristics
    - Set up custom prompts and conversation styles

4.  **Audio Processing:** For manipulating existing audio:

    - **Audio Isolation:** Separate speech from background noise and music
    - **Voice Conversion:** Transform audio to sound like a different voice or character
    - **Transcription:** Convert speech to text with speaker identification
    - **Sound Generation:** Create sound effects and soundscapes from text descriptions

5.  **Present Results:** Always provide clear information about:
    - Where generated audio files are saved
    - Voice IDs and names for future reference
    - Character and credit costs for transparency
    - Quality settings and parameters used

## Important Instructions

- **Follow Tool Instructions:** The descriptions for each tool are very detailed and contain **CRITICAL RULES** and best practices. You must read, understand, and follow them precisely.
- **Credit Awareness:** ElevenLabs tools consume credits. Be transparent about credit costs and help users make informed decisions about quality vs. cost trade-offs.
- **Handle Ambiguity:** If a user's request is ambiguous (e.g., which voice to use, what quality level), ask for clarification or offer intelligent defaults with explanations.
- **Provide Context:** When presenting generated audio, include relevant metadata like voice name, model used, file location, and any special settings applied.
- **Do Not Hallucinate:** Never invent voice IDs, file paths, or capabilities. If a tool call fails or returns an error, report it clearly to the user and suggest alternatives.
- **Be Creative:** When designing voices or soundscapes, be creative and offer multiple variations to give users choices.
- **Offer Feedback Channel:** If users encounter issues or have feature requests, they can reach out to ElevenLabs support or community channels.
```

## CHANNEL: tool descriptions (coverage=full)

Всего инструментов: 27 (<= 40, включены все). Описания приведены дословно из исходника; там, где описание — f-string, оставлена исходная запись с подстановкой `{get_output_mode_description(output_mode)}` (значение зависит от env `ELEVENLABS_MCP_OUTPUT_MODE`, см. конец раздела).

### text_to_speech (server.py:255)

```
f"""Convert text to speech with a given voice. {get_output_mode_description(output_mode)}.
    
    Only one of voice_id or voice_name can be provided. If none are provided, the default voice will be used.

    ⚠️ COST WARNING: This tool makes an API call to ElevenLabs which may incur costs. Only use when explicitly requested by the user.

     Args:
        text (str): The text to convert to speech.
        voice_name (str, optional): The name of the voice to use.
        model_id (str, optional): The model ID to use for speech synthesis. Options include:
            - eleven_v3: High quality model with most expressive voices
            - eleven_multilingual_v2: High quality multilingual model (29 languages)
            - eleven_flash_v2_5: Fastest model with ultra-low latency (32 languages)
            - eleven_turbo_v2_5: Balanced quality and speed (32 languages)
            - eleven_flash_v2: Fast English-only model
            - eleven_turbo_v2: Balanced English-only model
            Defaults to eleven_multilingual_v2 or environment variable ELEVENLABS_MODEL_ID.
        stability (float, optional): Stability of the generated audio. Determines how stable the voice is and the randomness between each generation. Lower values introduce broader emotional range for the voice. Higher values can result in a monotonous voice with limited emotion. Range is 0 to 1.
        similarity_boost (float, optional): Similarity boost of the generated audio. Determines how closely the AI should adhere to the original voice when attempting to replicate it. Range is 0 to 1.
        style (float, optional): Style of the generated audio. Determines the style exaggeration of the voice. This setting attempts to amplify the style of the original speaker. It does consume additional computational resources and might increase latency if set to anything other than 0. Range is 0 to 1.
        use_speaker_boost (bool, optional): Use speaker boost of the generated audio. This setting boosts the similarity to the original speaker. Using this setting requires a slightly higher computational load, which in turn increases latency.
        speed (float, optional): Speed of the generated audio. Controls the speed of the generated speech. Values range from 0.7 to 1.2, with 1.0 being the default speed. Lower values create slower, more deliberate speech while higher values produce faster-paced speech. Extreme values can impact the quality of the generated speech. Range is 0.7 to 1.2.
        output_directory (str, optional): Directory where files should be saved (only used when saving files).
            Defaults to $HOME/Desktop if not provided.
        language: ISO 639-1 language code for the voice.
        output_format (str, optional): Output format of the generated audio. Formatted as codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at 32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate requires you to be subscribed to Creator tier or above. PCM with 44.1kHz sample rate requires you to be subscribed to Pro tier or above. Note that the μ-law format (sometimes written mu-law, often approximated as u-law) is commonly used for Twilio audio inputs.
            Defaults to "mp3_44100_128". Must be one of:
            mp3_22050_32
            mp3_44100_32
            mp3_44100_64
            mp3_44100_96
            mp3_44100_128
            mp3_44100_192
            pcm_8000
            pcm_16000
            pcm_22050
            pcm_24000
            pcm_44100
            ulaw_8000
            alaw_8000
            opus_48000_32
            opus_48000_64
            opus_48000_96
            opus_48000_128
            opus_48000_192

    Returns:
        Text content with file path or MCP resource with audio data, depending on output mode.
    """
```

### speech_to_text (server.py:339)

```
f"""Transcribe speech from an audio file. When save_transcript_to_file=True: {get_output_mode_description(output_mode)}. When return_transcript_to_client_directly=True, always returns text directly regardless of output mode.

    ⚠️ COST WARNING: This tool makes an API call to ElevenLabs which may incur costs. Only use when explicitly requested by the user.

    Args:
        file_path: Path to the audio file to transcribe
        language_code: ISO 639-3 language code for transcription. If not provided, the language will be detected automatically.
        diarize: Whether to diarize the audio file. If True, which speaker is currently speaking will be annotated in the transcription.
        save_transcript_to_file: Whether to save the transcript to a file.
        return_transcript_to_client_directly: Whether to return the transcript to the client directly.
        output_directory: Directory where files should be saved (only used when saving files).
            Defaults to $HOME/Desktop if not provided.

    Returns:
        TextContent containing the transcription or MCP resource with transcript data.
    """
```

### text_to_sound_effects (server.py:430)

```
f"""Convert text description of a sound effect to sound effect with a given duration. {get_output_mode_description(output_mode)}.
    
    Duration must be between 0.5 and 5 seconds.

    ⚠️ COST WARNING: This tool makes an API call to ElevenLabs which may incur costs. Only use when explicitly requested by the user.

    Args:
        text: Text description of the sound effect
        duration_seconds: Duration of the sound effect in seconds
        output_directory: Directory where files should be saved (only used when saving files).
            Defaults to $HOME/Desktop if not provided.
        loop: Whether to loop the sound effect. Defaults to False.
        output_format (str, optional): Output format of the generated audio. Formatted as codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at 32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate requires you to be subscribed to Creator tier or above. PCM with 44.1kHz sample rate requires you to be subscribed to Pro tier or above. Note that the μ-law format (sometimes written mu-law, often approximated as u-law) is commonly used for Twilio audio inputs.
            Defaults to "mp3_44100_128". Must be one of:
            mp3_22050_32
            mp3_44100_32
            mp3_44100_64
            mp3_44100_96
            mp3_44100_128
            mp3_44100_192
            pcm_8000
            pcm_16000
            pcm_22050
            pcm_24000
            pcm_44100
            ulaw_8000
            alaw_8000
            opus_48000_32
            opus_48000_64
            opus_48000_96
            opus_48000_128
            opus_48000_192
    """
```

### search_voices (server.py:469)

```
"""
    Search for existing voices, a voice that has already been added to the user's ElevenLabs voice library.
    Searches in name, description, labels and category.

    Args:
        search: Search term to filter voices by. Searches in name, description, labels and category.
        sort: Which field to sort by. `created_at_unix` might not be available for older voices.
        sort_direction: Sort order, either ascending or descending.

    Returns:
        List of voices that match the search criteria.
    """
```

### list_models (server.py:487)

```
"List all available models"
```

### get_voice (server.py:506)

```
"Get details of a specific voice"
```

### voice_clone (server.py:524)

```
"""Create an instant voice clone of a voice using provided audio files.

    ⚠️ COST WARNING: This tool makes an API call to ElevenLabs which may incur costs. Only use when explicitly requested by the user.
    """
```

### isolate_audio (server.py:551)

```
f"""Isolate audio from a file. {get_output_mode_description(output_mode)}.

    ⚠️ COST WARNING: This tool makes an API call to ElevenLabs which may incur costs. Only use when explicitly requested by the user.
    """
```

### check_subscription (server.py:572)

```
"Check the current subscription status. Could be used to measure the usage of the API."
```

### create_agent (server.py:603)

```
"""Create a conversational AI agent with custom configuration.

    ⚠️ COST WARNING: This tool makes an API call to ElevenLabs which may incur costs. Only use when explicitly requested by the user.

    Args:
        name: Name of the agent
        first_message: First message the agent will say i.e. "Hi, how can I help you today?"
        system_prompt: System prompt for the agent
        voice_id: ID of the voice to use for the agent
        language: ISO 639-1 language code for the agent
        llm: LLM to use for the agent
        temperature: Temperature for the agent. The lower the temperature, the more deterministic the agent's responses will be. Range is 0 to 1.
        max_tokens: Maximum number of tokens to generate.
        asr_quality: Quality of the ASR. `high` or `low`.
        model_id: ID of the ElevenLabs model to use for the agent.
        optimize_streaming_latency: Optimize streaming latency. Range is 0 to 4.
        stability: Stability for the agent. Range is 0 to 1.
        similarity_boost: Similarity boost for the agent. Range is 0 to 1.
        turn_timeout: Timeout for the agent to respond in seconds. Defaults to 7 seconds.
        max_duration_seconds: Maximum duration of a conversation in seconds. Defaults to 600 seconds (10 minutes).
        record_voice: Whether to record the agent's voice.
        retention_days: Number of days to retain the agent's data.
    """
```

### add_knowledge_base_to_agent (server.py:670)

```
"""Add a knowledge base to ElevenLabs workspace. Allowed types are epub, pdf, docx, txt, html.

    ⚠️ COST WARNING: This tool makes an API call to ElevenLabs which may incur costs. Only use when explicitly requested by the user.

    Args:
        agent_id: ID of the agent to add the knowledge base to.
        knowledge_base_name: Name of the knowledge base.
        url: URL of the knowledge base.
        input_file_path: Path to the file to add to the knowledge base.
        text: Text to add to the knowledge base.
    """
```

### list_agents (server.py:742)

```
"List all available conversational AI agents"
```

### get_agent (server.py:764)

```
"Get details about a specific conversational AI agent"
```

### get_conversation (server.py:793)

```
"""Gets conversation with transcript. Returns: conversation details and full transcript. Use when: analyzing completed agent conversations.

    Args:
        conversation_id: The unique identifier of the conversation to retrieve, you can get the ids from the list_conversations tool.
    """
```

### simulate_conversation (server.py:866)

```
"""Simulate a text conversation between a conversational AI agent and a
    simulated user. Runs the full conversation and returns the transcript plus analysis.

    Use this to test agent behaviour, evaluate prompts, and catch failure modes without
    a live call. The simulated user follows the persona you describe.

    ⚠️ COST WARNING: This tool makes an API call to ElevenLabs which may incur costs.
    Only use when explicitly requested by the user.

    Args:
        agent_id: ID of the agent to test. Use list_agents to find IDs.
        simulated_user_prompt: Instructions for how the simulated user should behave.
            Example: "You are a frustrated customer who cannot find the cancel button."
        first_message: Optional opening message to kick off the conversation.
        extra_evaluation_criteria: Optional list of dicts, each with:
            - id (str): unique key e.g. "issue_resolved"
            - name (str): human label e.g. "Issue Resolved"
            - conversation_goal_prompt (str): the assertion to check
              e.g. "The agent fully resolved the user's issue."
            - use_knowledge_base (bool, optional): whether the evaluator should
              reference the agent's knowledge base when judging. Defaults to False.
        max_turns: Maximum conversation turns. Defaults to 10.
    """
```

### list_conversations (server.py:957)

```
"""Lists agent conversations. Returns: conversation list with metadata. Use when: asked about conversation history.

    Args:
        agent_id (str, optional): Filter conversations by specific agent ID
        cursor (str, optional): Pagination cursor for retrieving next page of results
        call_start_before_unix (int, optional): Filter conversations that started before this Unix timestamp
        call_start_after_unix (int, optional): Filter conversations that started after this Unix timestamp
        page_size (int, optional): Number of conversations to return per page (1-100, defaults to 30)
        max_length (int, optional): Maximum character length of the response text (defaults to 10000)
    """
```

### speech_to_speech (server.py:1026)

```
f"""Transform audio from one voice to another using provided audio files. {get_output_mode_description(output_mode)}.

    ⚠️ COST WARNING: This tool makes an API call to ElevenLabs which may incur costs. Only use when explicitly requested by the user.
    """
```

### text_to_voice (server.py:1074)

```
f"""Create voice previews from a text prompt. Creates three previews with slight variations. {get_output_mode_description(output_mode)}.

    If no text is provided, the tool will auto-generate text.

    Voice preview files are saved as: voice_design_(generated_voice_id)_(timestamp).mp3

    Example file name: voice_design_Ya2J5uIa5Pq14DNPsbC1_20250403_164949.mp3

    ⚠️ COST WARNING: This tool makes an API call to ElevenLabs which may incur costs. Only use when explicitly requested by the user.
    """
```

### create_voice_from_preview (server.py:1118)

```
"""Add a generated voice to the voice library. Uses the voice ID from the `text_to_voice` tool.

    ⚠️ COST WARNING: This tool makes an API call to ElevenLabs which may incur costs. Only use when explicitly requested by the user.
    """
```

### make_outbound_call (server.py:1159)

```
"""Make an outbound call using an ElevenLabs agent. Automatically detects provider type (Twilio or SIP trunk) and uses the appropriate API.

    ⚠️ COST WARNING: This tool makes an API call to ElevenLabs which may incur costs. Only use when explicitly requested by the user.

    Args:
        agent_id: The ID of the agent that will handle the call
        agent_phone_number_id: The ID of the phone number to use for the call
        to_number: The phone number to call (E.164 format: +1xxxxxxxxxx)

    Returns:
        TextContent containing information about the call
    """
```

### search_voice_library (server.py:1202)

```
"""Search for a voice across the entire ElevenLabs voice library.

    Args:
        page: Page number to return (0-indexed)
        page_size: Number of voices to return per page (1-100)
        search: Search term to filter voices by

    Returns:
        TextContent containing information about the shared voices
    """
```

### list_phone_numbers (server.py:1265)

```
"List all phone numbers associated with the ElevenLabs account"
```

### play_audio (server.py:1298)

```
"Play an audio file. Supports WAV and MP3 formats."
```

### compose_music (server.py:1325)

```
f"""Convert a prompt to music and save the output audio file to a given directory.
    Directory is optional, if not provided, the output file will be saved to $HOME/Desktop. {get_output_mode_description(output_mode)}.

    Two models are supported:
    - music_v2 (default): latest model. Composition plans use a `chunks` array where each chunk is either a `GenerationChunk` (text, duration_ms, positive_styles, negative_styles, context_adherence, optional conditioning_ref + condition_strength) or an `AudioRefChunk` ({{song_id, range: {{start_ms, end_ms}}}}) for inpainting. Inpainting also requires the source song to have been stored — call this tool with store_for_inpainting=True or use upload_music_for_inpainting first to get a song_id.
    - music_v1: legacy model. Composition plans use positive_global_styles, negative_global_styles, sections.

    Args:
        prompt: Prompt to convert to music. Must provide either prompt or composition_plan.
        output_directory: Directory to save the output audio file
        composition_plan: Composition plan dict. Shape depends on model_id (see above). Must provide either prompt or composition_plan.
        music_length_ms: Length of the generated music in milliseconds (3000-600000). Cannot be used if composition_plan is provided.
        model_id: Which music model to use. One of "music_v1" or "music_v2". Defaults to "music_v2".
        force_instrumental: If True, the model will avoid generating lyrics/vocals.
        store_for_inpainting: If True, the generated song is stored server-side and the returned song_id can be used in later inpainting calls (as an AudioRefChunk.song_id, or conditioning_ref).
        seed: Optional integer seed for reproducible generation (music_v2 only).

    ⚠️ COST WARNING: This tool makes an API call to ElevenLabs which may incur costs. Only use when explicitly requested by the user."""
```

### create_composition_plan (server.py:1402)

```
"""Create a composition plan for music generation. Usage of this endpoint does not cost any credits but is subject to rate limiting depending on your tier. Composition plans can be used when generating music with the compose_music tool.

    The returned plan shape depends on model_id:
    - music_v2 (default): `{"chunks": [GenerationChunk | AudioRefChunk, ...]}`. Each GenerationChunk has `text`, `duration_ms`, `positive_styles`, `negative_styles`, `context_adherence` and optional `conditioning_ref` + `condition_strength`. AudioRefChunks reference a stored song via `song_id` and `range: {start_ms, end_ms}` for inpainting.
    - music_v1: `{"positive_global_styles": [...], "negative_global_styles": [...], "sections": [...]}`.

    Args:
        prompt: Prompt to create a composition plan for
        music_length_ms: The length of the composition plan to generate in milliseconds. Must be between 10000ms and 300000ms. Optional - if not provided, the model will choose a length based on the prompt.
        source_composition_plan: An optional composition plan dict to use as a source for the new composition plan. Should match the shape of the model_id you request.
        model_id: Which music model to plan for. One of "music_v1" or "music_v2". Defaults to "music_v2".
    """
```

### video_to_music (server.py:1441)

```
f"""Generate background music for one or more video files. {get_output_mode_description(output_mode)}.

    The videos are concatenated server-side in the order provided; the generated score targets the combined duration. Constraints: 1-10 videos per call, combined size <= 200 MB, combined duration <= 600 seconds.

    Args:
        input_file_paths: Paths to the video files. Order is preserved.
        description: Optional natural-language direction for the music (e.g. "Build suspense, then resolve with a warm cinematic finish.").
        tags: Optional list of up to 10 short style cues (e.g. ["cinematic", "suspenseful", "uplifting"]).
        model_id: Which music model to use. One of "music_v1" or "music_v2". Defaults to "music_v2".
        output_directory: Directory to save the generated audio file. Defaults to $HOME/Desktop.

    ⚠️ COST WARNING: This tool makes an API call to ElevenLabs which may incur costs. Only use when explicitly requested by the user.
    """
```

### upload_music_for_inpainting (server.py:1492)

```
"""Upload an existing audio file to ElevenLabs so it can be referenced in music_v2 inpainting workflows. Returns a song_id you can plug into a composition plan's AudioRefChunks (or a generation chunk's conditioning_ref) to edit or extend the track via the compose_music tool.

    Optionally extracts a composition plan from the uploaded audio so you have a starting point to mutate.

    Note: this endpoint is gated to enterprise customers with inpainting access.

    Args:
        input_file_path: Path to a local audio file to upload.
        extract_composition_plan: Which model to extract a composition plan for ("music_v1" or "music_v2"). Pass None to skip extraction. Defaults to "music_v2".

    ⚠️ COST WARNING: This tool makes an API call to ElevenLabs which may incur costs. Only use when explicitly requested by the user.
    """
```

### Подстановка в f-string описаниях: `get_output_mode_description(output_mode)` (utils.py:512)

```
    if output_mode == "files":
        return "Saves output file to directory (default: $HOME/Desktop)"
    elif output_mode == "resources":
        return "Returns output as base64-encoded MCP resource"
    elif output_mode == "both":
        return "Saves file to directory (default: $HOME/Desktop) AND returns as base64-encoded MCP resource"
    else:
        return "Output behavior depends on ELEVENLABS_MCP_OUTPUT_MODE setting"
```
