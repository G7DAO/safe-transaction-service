# flake8: noqa E501
import json

conditional_token_abi = json.loads(
    '[{"constant":true,"inputs":[{"name":"owner","type":"address"},{"name":"id","type":"uint256"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"bytes32"},{"name":"","type":"uint256"}],"name":"payoutNumerators","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"from","type":"address"},{"name":"to","type":"address"},{"name":"ids","type":"uint256[]"},{"name":"values","type":"uint256[]"},{"name":"data","type":"bytes"}],"name":"safeBatchTransferFrom","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"owners","type":"address[]"},{"name":"ids","type":"uint256[]"}],"name":"balanceOfBatch","outputs":[{"name":"","type":"uint256[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"operator","type":"address"},{"name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"bytes32"}],"name":"payoutDenominator","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"owner","type":"address"},{"name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"from","type":"address"},{"name":"to","type":"address"},{"name":"id","type":"uint256"},{"name":"value","type":"uint256"},{"name":"data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"conditionId","type":"bytes32"},{"indexed":true,"name":"oracle","type":"address"},{"indexed":true,"name":"questionId","type":"bytes32"},{"indexed":false,"name":"outcomeSlotCount","type":"uint256"}],"name":"ConditionPreparation","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"conditionId","type":"bytes32"},{"indexed":true,"name":"oracle","type":"address"},{"indexed":true,"name":"questionId","type":"bytes32"},{"indexed":false,"name":"outcomeSlotCount","type":"uint256"},{"indexed":false,"name":"payoutNumerators","type":"uint256[]"}],"name":"ConditionResolution","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"stakeholder","type":"address"},{"indexed":false,"name":"collateralToken","type":"address"},{"indexed":true,"name":"parentCollectionId","type":"bytes32"},{"indexed":true,"name":"conditionId","type":"bytes32"},{"indexed":false,"name":"partition","type":"uint256[]"},{"indexed":false,"name":"amount","type":"uint256"}],"name":"PositionSplit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"stakeholder","type":"address"},{"indexed":false,"name":"collateralToken","type":"address"},{"indexed":true,"name":"parentCollectionId","type":"bytes32"},{"indexed":true,"name":"conditionId","type":"bytes32"},{"indexed":false,"name":"partition","type":"uint256[]"},{"indexed":false,"name":"amount","type":"uint256"}],"name":"PositionsMerge","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"redeemer","type":"address"},{"indexed":true,"name":"collateralToken","type":"address"},{"indexed":true,"name":"parentCollectionId","type":"bytes32"},{"indexed":false,"name":"conditionId","type":"bytes32"},{"indexed":false,"name":"indexSets","type":"uint256[]"},{"indexed":false,"name":"payout","type":"uint256"}],"name":"PayoutRedemption","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"operator","type":"address"},{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"id","type":"uint256"},{"indexed":false,"name":"value","type":"uint256"}],"name":"TransferSingle","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"operator","type":"address"},{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"ids","type":"uint256[]"},{"indexed":false,"name":"values","type":"uint256[]"}],"name":"TransferBatch","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"operator","type":"address"},{"indexed":false,"name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"value","type":"string"},{"indexed":true,"name":"id","type":"uint256"}],"name":"URI","type":"event"},{"constant":false,"inputs":[{"name":"oracle","type":"address"},{"name":"questionId","type":"bytes32"},{"name":"outcomeSlotCount","type":"uint256"}],"name":"prepareCondition","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"questionId","type":"bytes32"},{"name":"payouts","type":"uint256[]"}],"name":"reportPayouts","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"collateralToken","type":"address"},{"name":"parentCollectionId","type":"bytes32"},{"name":"conditionId","type":"bytes32"},{"name":"partition","type":"uint256[]"},{"name":"amount","type":"uint256"}],"name":"splitPosition","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"collateralToken","type":"address"},{"name":"parentCollectionId","type":"bytes32"},{"name":"conditionId","type":"bytes32"},{"name":"partition","type":"uint256[]"},{"name":"amount","type":"uint256"}],"name":"mergePositions","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"collateralToken","type":"address"},{"name":"parentCollectionId","type":"bytes32"},{"name":"conditionId","type":"bytes32"},{"name":"indexSets","type":"uint256[]"}],"name":"redeemPositions","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"conditionId","type":"bytes32"}],"name":"getOutcomeSlotCount","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"oracle","type":"address"},{"name":"questionId","type":"bytes32"},{"name":"outcomeSlotCount","type":"uint256"}],"name":"getConditionId","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"name":"parentCollectionId","type":"bytes32"},{"name":"conditionId","type":"bytes32"},{"name":"indexSet","type":"uint256"}],"name":"getCollectionId","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"collateralToken","type":"address"},{"name":"collectionId","type":"bytes32"}],"name":"getPositionId","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"}]'
)
market_maker_abi = json.loads(
    '[{"constant":true,"inputs":[{"name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"resume","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"pmSystem","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"outcomeTokenAmounts","type":"int256[]"},{"name":"collateralLimit","type":"int256"}],"name":"trade","outputs":[{"name":"netCost","type":"int256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"close","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"withdrawFees","outputs":[{"name":"fees","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"renounceOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"pause","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"fundingChange","type":"int256"}],"name":"changeFunding","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"isOwner","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"whitelist","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"outcomeTokenCost","type":"uint256"}],"name":"calcMarketFee","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"collateralToken","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_operator","type":"address"},{"name":"","type":"address"},{"name":"","type":"uint256[]"},{"name":"","type":"uint256[]"},{"name":"","type":"bytes"}],"name":"onERC1155BatchReceived","outputs":[{"name":"","type":"bytes4"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"stage","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"funding","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"conditionIds","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"atomicOutcomeSlotCount","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"fee","outputs":[{"name":"","type":"uint64"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_fee","type":"uint64"}],"name":"changeFee","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"operator","type":"address"},{"name":"","type":"address"},{"name":"","type":"uint256"},{"name":"","type":"uint256"},{"name":"","type":"bytes"}],"name":"onERC1155Received","outputs":[{"name":"","type":"bytes4"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"FEE_RANGE","outputs":[{"name":"","type":"uint64"}],"payable":false,"stateMutability":"view","type":"function"},{"anonymous":false,"inputs":[{"indexed":false,"name":"initialFunding","type":"uint256"}],"name":"AMMCreated","type":"event"},{"anonymous":false,"inputs":[],"name":"AMMPaused","type":"event"},{"anonymous":false,"inputs":[],"name":"AMMResumed","type":"event"},{"anonymous":false,"inputs":[],"name":"AMMClosed","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"fundingChange","type":"int256"}],"name":"AMMFundingChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"newFee","type":"uint64"}],"name":"AMMFeeChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"fees","type":"uint256"}],"name":"AMMFeeWithdrawal","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"transactor","type":"address"},{"indexed":false,"name":"outcomeTokenAmounts","type":"int256[]"},{"indexed":false,"name":"outcomeTokenNetCost","type":"int256"},{"indexed":false,"name":"marketFees","type":"uint256"}],"name":"AMMOutcomeTokenTrade","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"previousOwner","type":"address"},{"indexed":true,"name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"constant":true,"inputs":[{"name":"outcomeTokenAmounts","type":"int256[]"}],"name":"calcNetCost","outputs":[{"name":"netCost","type":"int256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"outcomeTokenIndex","type":"uint8"}],"name":"calcMarginalPrice","outputs":[{"name":"price","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]'
)
market_maker_factory_abi = json.loads(
    '[{"constant":true,"inputs":[],"name":"implementationMaster","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"creator","type":"address"},{"indexed":false,"name":"lmsrMarketMaker","type":"address"},{"indexed":false,"name":"pmSystem","type":"address"},{"indexed":false,"name":"collateralToken","type":"address"},{"indexed":false,"name":"conditionIds","type":"bytes32[]"},{"indexed":false,"name":"fee","type":"uint64"},{"indexed":false,"name":"funding","type":"uint256"}],"name":"LMSRMarketMakerCreation","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"previousOwner","type":"address"},{"indexed":true,"name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"initialFunding","type":"uint256"}],"name":"AMMCreated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"target","type":"address"},{"indexed":false,"name":"clone","type":"address"}],"name":"CloneCreated","type":"event"},{"constant":false,"inputs":[{"name":"consData","type":"bytes"}],"name":"cloneConstructor","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"pmSystem","type":"address"},{"name":"collateralToken","type":"address"},{"name":"conditionIds","type":"bytes32[]"},{"name":"fee","type":"uint64"},{"name":"whitelist","type":"address"},{"name":"funding","type":"uint256"}],"name":"createLMSRMarketMaker","outputs":[{"name":"lmsrMarketMaker","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]'
)
