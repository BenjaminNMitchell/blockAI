# Config file for block AI

BASH_PROFILE="${HOME}/.bash_profile"
mkdir -p "${HOME}/.config/block_ai"
CONFIG_FILE="${HOME}/.config/block_ai/block_ai_config.sh"
echo "Writing to $BASH_PROFILE"
echo "       and $CONFIG_FILE"


echo "" >> $BASH_PROFILE
echo "# Written BY BlockAI" >> $BASH_PROFILE
echo "source $CONFIG_FILE" >> $BASH_PROFILE
echo "export BLOCK_AI_ROOT=$(pwd)" >| $CONFIG_FILE

